"""Tests for Level 3: OR Patterns and Guards."""

import pytest
from adventure.game import create_game

from adventure.handlers_level3 import handle_command


@pytest.fixture
def player():
    return create_game()


class TestDirectionAliases:
    def test_go_n_alias_works(self, player):
        result = handle_command(player, ["go", "n"])
        assert player.current_room.name == "library"
        assert "library" in result

    def test_go_s_alias_works(self, player):
        handle_command(player, ["go", "n"])  # go north first
        result = handle_command(player, ["go", "s"])  # then south
        assert player.current_room.name == "entrance hall"

    def test_go_e_alias_works(self, player):
        result = handle_command(player, ["go", "e"])
        assert player.current_room.name == "kitchen"

    def test_full_direction_still_works(self, player):
        result = handle_command(player, ["go", "north"])
        assert player.current_room.name == "library"


class TestCommandSynonyms:
    def test_get_works(self, player):
        handle_command(player, ["go", "north"])
        result = handle_command(player, ["get", "book"])
        assert player.has_item("book")

    def test_take_still_works(self, player):
        handle_command(player, ["go", "north"])
        result = handle_command(player, ["take", "book"])
        assert player.has_item("book")

    def test_grab_also_works(self, player):
        handle_command(player, ["go", "north"])
        result = handle_command(player, ["grab", "book"])
        assert player.has_item("book")


class TestGuards:
    def test_guard_validates_exits(self, player):
        """Guard should prevent moving to nonexistent exits."""
        result = handle_command(player, ["go", "west"])
        assert player.current_room.name == "entrance hall"
        assert "can't go" in result.lower() or "can't" in result.lower()

    def test_guard_allows_valid_exit(self, player):
        result = handle_command(player, ["go", "north"])
        assert player.current_room.name == "library"

    def test_go_with_direction_alias_invalid(self, player):
        result = handle_command(player, ["go", "up"])
        assert player.current_room.name == "entrance hall"
        assert "can't go" in result.lower() or "can't" in result.lower()


class TestExamineStillWorks:
    def test_examine_in_room(self, player):
        handle_command(player, ["go", "east"])
        result = handle_command(player, ["examine", "key"])
        assert "key" in result.lower() or "rusty" in result.lower()


class TestWildcard:
    def test_unknown_multiword_command(self, player):
        result = handle_command(player, ["fly", "away"])
        assert "don't understand" in result.lower() or "unknown" in result.lower()

    def test_level1_commands_still_work(self, player):
        result = handle_command(player, ["look"])
        assert "entrance hall" in result

    def test_quit_still_works(self, player):
        handle_command(player, ["quit"])
        assert player.running is False
