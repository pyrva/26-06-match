"""Complete handlers — fully implemented reference solution.

This module contains all four levels of pattern matching fully implemented.
It serves as the solution reference and enables the game to run end-to-end.

Use this file to:
1. See how each exercise level is solved
2. Run the game with a working command handler
3. Verify that all tests pass
"""

from __future__ import annotations

from adventure.events import Click, KeyPress, Quit, TextCommand
from adventure.game import Player

# ---------------------------------------------------------------------------
# Level 1: Literal and Wildcard Patterns
# ---------------------------------------------------------------------------


def handle_level1(player: Player, command: str) -> str:
    """Handle single-word commands with literal and wildcard patterns."""
    help_text = (
        "Available commands:\n"
        "  look       — look around the room\n"
        "  go <dir>   — move in a direction (north, south, east, west)\n"
        "  take <item>— pick up an item\n"
        "  examine <t>— look at an item or feature\n"
        "  inventory  — check your inventory\n"
        "  help       — show this help text\n"
        "  quit       — exit the game"
    )

    match command:
        case "quit":
            player.running = False
            return "Goodbye!"
        case "look":
            return player.current_room.look()
        case "help":
            return help_text
        case "inventory":
            return player.show_inventory()
        case _:
            return "I don't understand that command."


# ---------------------------------------------------------------------------
# Level 2: Capture and Sequence Patterns
# ---------------------------------------------------------------------------


def _find_item(name: str, player: Player):
    """Find an item by name in the room or player inventory."""
    for item in player.current_room.items:
        if item.name == name:
            return item, "room"
    for item in player.inventory:
        if item.name == name:
            return item, "inventory"
    return None, None


def handle_level2(player: Player, words: list[str]) -> str:
    """Handle multi-word commands with capture and sequence patterns."""
    # Delegate single-word commands to Level 1
    if len(words) == 1:
        result = handle_level1(player, words[0])
        if "don't understand" not in result.lower():
            return result

    match words:
        case ["go", direction]:
            if direction in player.current_room.exits:
                player.current_room = player.current_room.exits[direction]
                return player.current_room.look()
            return f"You can't go {direction}."

        case ["take", item_name] | ["get", item_name] | ["grab", item_name]:
            if player.has_item(item_name):
                return f"You already have the {item_name}."
            for item in player.current_room.items:
                if item.name == item_name:
                    player.current_room.remove_item(item)
                    player.add_to_inventory(item)
                    return f"You take the {item_name}."
            return f"You don't see {item_name} here."

        case ["examine", target]:
            for item in player.current_room.items:
                if item.name == target:
                    return item.description
            for item in player.inventory:
                if item.name == target:
                    return item.description
            return f"You don't see {target} here."

        case _:
            return "I don't understand that command."


# ---------------------------------------------------------------------------
# Level 3: OR Patterns and Guards
# ---------------------------------------------------------------------------

DIRECTION_ALIASES = {"n": "north", "s": "south", "e": "east", "w": "west"}


def handle_level3(player: Player, words: list[str]) -> str:
    """Handle commands with OR patterns and guards."""
    # Delegate single-word commands to Level 1
    if len(words) == 1:
        result = handle_level1(player, words[0])
        if "don't understand" not in result.lower():
            return result

    match words:
        # Direction aliases using OR patterns with 'as'
        case ["go", ("north" | "n") as direction]:
            actual = DIRECTION_ALIASES.get(direction, direction)
            player.current_room = player.current_room.exits[actual]
            return player.current_room.look()

        case ["go", ("south" | "s") as direction]:
            actual = DIRECTION_ALIASES.get(direction, direction)
            player.current_room = player.current_room.exits[actual]
            return player.current_room.look()

        case ["go", ("east" | "e") as direction]:
            actual = DIRECTION_ALIASES.get(direction, direction)
            player.current_room = player.current_room.exits[actual]
            return player.current_room.look()

        case ["go", ("west" | "w") as direction]:
            actual = DIRECTION_ALIASES.get(direction, direction)
            player.current_room = player.current_room.exits[actual]
            return player.current_room.look()

        # Guard: any valid exit direction
        case ["go", direction] if direction in player.current_room.exits:
            player.current_room = player.current_room.exits[direction]
            return player.current_room.look()

        # Catch-all for invalid directions (must come after the guarded case)
        case ["go", _]:
            return "You can't go that way."

        # Command synonyms using OR patterns
        case ["get" | "take" | "grab", item_name]:
            if player.has_item(item_name):
                return f"You already have the {item_name}."
            for item in player.current_room.items:
                if item.name == item_name:
                    player.current_room.remove_item(item)
                    player.add_to_inventory(item)
                    return f"You take the {item_name}."
            return f"You don't see {item_name} here."

        case ["examine", target]:
            for item in player.current_room.items:
                if item.name == target:
                    return item.description
            for item in player.inventory:
                if item.name == target:
                    return item.description
            return f"You don't see {target} here."

        case _:
            return "I don't understand that command."


# ---------------------------------------------------------------------------
# Level 4: Class Patterns
# ---------------------------------------------------------------------------

WASD_MAP = {"w": "north", "a": "west", "s": "south", "d": "east"}


def handle_level4(player: Player, event) -> str:
    """Handle events using class patterns."""
    match event:
        case Click((x, y)):
            if (x, y) == (0, 0):
                return "Nothing interesting there."
            return f"You click at position ({x}, {y})."

        case KeyPress("q") | KeyPress("Q"):
            player.running = False
            return "Goodbye!"

        case KeyPress(key) if key in WASD_MAP:
            return handle_level3(player, ["go", WASD_MAP[key]])

        case KeyPress(key):
            return f"Unknown key: {key}"

        case TextCommand(text):
            words = text.strip().split()
            return handle_level3(player, words)

        case Quit():
            player.running = False
            return "Goodbye!"


# ---------------------------------------------------------------------------
# Unified entry point
# ---------------------------------------------------------------------------


def handle_command(player: Player, words: list[str]) -> str:
    """Main command handler — delegates to the appropriate level.

    This function is used by the game engine's run_command() entry point.
    It uses the most capable handler (Level 3) for text commands.
    """
    return handle_level3(player, words)
