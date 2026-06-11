"""Tests for Level 1: Literal and Wildcard Patterns."""

import pytest
from adventure.game import create_game

# Import the handler — tests will fail until participants implement it
from adventure.handlers_level1 import handle_command


@pytest.fixture
def player():
    """Create a fresh player for each test."""
    return create_game()


class TestQuitCommand:
    def test_quit_returns_goodbye(self, player):
        result = handle_command(player, "quit")
        assert "goodbye" in result.lower() or "Goodbye" in result

    def test_quit_stops_the_game(self, player):
        assert player.running is True
        handle_command(player, "quit")
        assert player.running is False


class TestLookCommand:
    def test_look_describes_current_room(self, player):
        result = handle_command(player, "look")
        assert "entrance hall" in result

    def test_look_shows_exits(self, player):
        result = handle_command(player, "look")
        assert "north" in result
        assert "east" in result


class TestHelpCommand:
    def test_help_returns_help_text(self, player):
        result = handle_command(player, "help")
        assert len(result) > 0
        # Help text should mention available commands
        assert "quit" in result.lower() or "look" in result.lower()


class TestInventoryCommand:
    def test_inventory_when_empty(self, player):
        result = handle_command(player, "inventory")
        assert "nothing" in result.lower() or "empty" in result.lower()

    def test_inventory_when_carrying_items(self, player):
        from adventure.game import Item
        player.add_to_inventory(Item("sword", "A sword."))
        result = handle_command(player, "inventory")
        assert "sword" in result


class TestWildcard:
    def test_unknown_command(self, player):
        result = handle_command(player, "fly")
        assert "don't understand" in result.lower() or "unknown" in result.lower()

    def test_another_unknown_command(self, player):
        result = handle_command(player, "dance")
        assert "don't understand" in result.lower() or "unknown" in result.lower()

    def test_nonsense_input(self, player):
        result = handle_command(player, "xyzzy")
        assert "don't understand" in result.lower() or "unknown" in result.lower()


class TestCaseSensitivity:
    """Pattern matching is case-sensitive — 'LOOK' should NOT match 'look'.

    This is a predict-then-run moment! Ask participants to predict what
    happens before running this test.
    """

    def test_uppercase_look_falls_to_wildcard(self, player):
        result = handle_command(player, "LOOK")
        # Should NOT return the room description — should be the wildcard response
        assert "entrance hall" not in result
        assert "don't understand" in result.lower() or "unknown" in result.lower()

    def test_mixed_case_quit_falls_to_wildcard(self, player):
        result = handle_command(player, "Quit")
        assert player.running is True  # Should NOT have quit
        assert "don't understand" in result.lower() or "unknown" in result.lower()
