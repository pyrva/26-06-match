"""Tests for Level 4: Class Patterns."""

import pytest

from adventure.events import Click, KeyPress, Quit, TextCommand
from adventure.game import create_game
from adventure.handlers_level4 import handle_event


@pytest.fixture
def player():
    return create_game()


class TestClickEvents:
    def test_click_returns_position(self, player):
        result = handle_event(player, Click((3, 7)))
        assert "3" in result and "7" in result

    def test_click_at_origin(self, player):
        result = handle_event(player, Click((0, 0)))
        assert "nothing" in result.lower() or "Nothing" in result

    def test_click_extracts_x_and_y(self, player):
        """Click((x, y)) should extract both coordinates."""
        result = handle_event(player, Click((5, 10)))
        assert "5" in result and "10" in result


class TestKeyPressQuit:
    def test_quit_lowercase_q(self, player):
        result = handle_event(player, KeyPress("q"))
        assert player.running is False
        assert "goodbye" in result.lower() or "Goodbye" in result

    def test_quit_uppercase_Q(self, player):
        result = handle_event(player, KeyPress("Q"))
        assert player.running is False
        assert "goodbye" in result.lower() or "Goodbye" in result


class TestKeyPressWASD:
    def test_w_moves_north(self, player):
        result = handle_event(player, KeyPress("w"))
        assert player.current_room.name == "library"

    def test_a_tries_west(self, player):
        """Entrance hall has no west exit, so the Level 3 guard catches it."""
        result = handle_event(player, KeyPress("a"))
        assert player.current_room.name == "entrance hall"  # didn't move
        assert "can't go" in result.lower() or "can't" in result.lower()

    def test_d_moves_east(self, player):
        result = handle_event(player, KeyPress("d"))
        assert player.current_room.name == "kitchen"

    def test_s_tries_south(self, player):
        """Entrance hall has no south exit."""
        result = handle_event(player, KeyPress("s"))
        assert player.current_room.name == "entrance hall"


class TestKeyPressUnknown:
    def test_unknown_key(self, player):
        result = handle_event(player, KeyPress("z"))
        assert "unknown" in result.lower()
        assert player.running is True  # didn't quit

    def test_number_key(self, player):
        result = handle_event(player, KeyPress("1"))
        assert "unknown" in result.lower()


class TestTextCommand:
    def test_text_command_go_north(self, player):
        result = handle_event(player, TextCommand("go north"))
        assert player.current_room.name == "library"

    def test_text_command_look(self, player):
        result = handle_event(player, TextCommand("look"))
        assert "entrance hall" in result

    def test_text_command_take(self, player):
        handle_event(player, TextCommand("go north"))
        result = handle_event(player, TextCommand("take book"))
        assert player.has_item("book")

    def test_text_command_uses_level3_aliases(self, player):
        """Text commands should use Level 3 handler (with aliases)."""
        result = handle_event(player, TextCommand("go n"))
        assert player.current_room.name == "library"


class TestQuitEvent:
    def test_quit_event(self, player):
        result = handle_event(player, Quit())
        assert player.running is False
        assert "goodbye" in result.lower() or "Goodbye" in result
