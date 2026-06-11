"""Tests for Level 2: Capture and Sequence Patterns."""

import pytest
from adventure.game import create_game

from adventure.handlers_level2 import handle_command


@pytest.fixture
def player():
    return create_game()


class TestGoCommand:
    def test_go_north_moves_to_library(self, player):
        result = handle_command(player, ["go", "north"])
        assert player.current_room.name == "library"
        assert "library" in result

    def test_go_east_moves_to_kitchen(self, player):
        result = handle_command(player, ["go", "east"])
        assert player.current_room.name == "kitchen"

    def test_go_invalid_direction(self, player):
        result = handle_command(player, ["go", "west"])
        assert player.current_room.name == "entrance hall"  # didn't move
        assert "can't go" in result.lower() or "can't" in result.lower()

    def test_go_south_from_entrance(self, player):
        result = handle_command(player, ["go", "south"])
        assert "can't go" in result.lower() or "can't" in result.lower()

    def test_go_then_go_back(self, player):
        handle_command(player, ["go", "north"])
        result = handle_command(player, ["go", "south"])
        assert player.current_room.name == "entrance hall"


class TestTakeCommand:
    def test_take_book_from_library(self, player):
        handle_command(player, ["go", "north"])  # go to library
        result = handle_command(player, ["take", "book"])
        assert "book" in result.lower()
        assert player.has_item("book")

    def test_take_removes_item_from_room(self, player):
        handle_command(player, ["go", "north"])
        handle_command(player, ["take", "book"])
        library = player.current_room
        assert not any(item.name == "book" for item in library.items)

    def test_take_item_already_in_inventory(self, player):
        handle_command(player, ["go", "north"])
        handle_command(player, ["take", "book"])
        result = handle_command(player, ["take", "book"])
        assert "already" in result.lower()

    def test_take_item_not_in_room(self, player):
        result = handle_command(player, ["take", "dragon"])
        assert "don't see" in result.lower() or "can't find" in result.lower()
        assert not player.has_item("dragon")


class TestExamineCommand:
    def test_examine_item_in_room(self, player):
        handle_command(player, ["go", "east"])  # kitchen has items
        result = handle_command(player, ["examine", "key"])
        assert "rusty" in result.lower() or "key" in result.lower()

    def test_examine_item_in_inventory(self, player):
        handle_command(player, ["go", "north"])
        handle_command(player, ["take", "book"])
        result = handle_command(player, ["examine", "book"])
        assert "book" in result.lower() or "leather" in result.lower()

    def test_examine_item_not_present(self, player):
        result = handle_command(player, ["examine", "unicorn"])
        assert "don't see" in result.lower() or "can't find" in result.lower()


class TestSequencePatterns:
    """Tests for sequence pattern edge cases — predict-then-run moments!"""

    def test_single_go_word_falls_through(self, player):
        """["go"] with no direction — sequence pattern requires exactly 2 elements."""
        result = handle_command(player, ["go"])
        # Should fall through to wildcard
        assert "don't understand" in result.lower() or "can't" in result.lower()

    def test_go_with_extra_words_falls_through(self, player):
        """["go", "north", "fast"] — sequence pattern for 2 elements won't match 3."""
        result = handle_command(player, ["go", "north", "fast"])
        # A case ["go", direction]: won't match 3-element lists!
        assert "don't understand" in result.lower() or "can't" in result.lower()

    def test_level1_commands_still_work(self, player):
        """Single-word commands should still be handled."""
        result = handle_command(player, ["look"])
        assert "entrance hall" in result

    def test_quit_still_works(self, player):
        result = handle_command(player, ["quit"])
        assert player.running is False
