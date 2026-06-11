"""Level 3: OR Patterns and Guards.

Now you'll add command aliases and conditional logic INSIDE the match block.
"""

from adventure.handlers_level1 import handle_command as level1_handle

DIRECTION_ALIASES = {"n": "north", "s": "south", "e": "east", "w": "west"}


def handle_command(player, words: list[str]) -> str:
    """Handle commands with OR patterns and guards."""
    if len(words) == 1:
        result = level1_handle(player, words[0])
        if "don't understand" not in result.lower():
            return result

    match words:
        # Direction aliases using OR patterns with 'as'
        case ["go", ("north" | "n") as direction]:
            actual = DIRECTION_ALIASES.get(direction, direction)
            player.current_room = player.current_room.exits[actual]
            return player.current_room.look()

        # TODO: Add OR patterns for south/s, east/e, west/w
        # HINT: Follow the same pattern as north/n above.

        # TODO: Add a guarded case for any valid exit direction
        # HINT: case ["go", direction] if direction in player.current_room.exits:

        # TODO: Add a catch-all for invalid directions
        # HINT: case ["go", _]:

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

        # TODO: Add examine case (from Level 2)

        case _:
            return "I don't understand that command."
