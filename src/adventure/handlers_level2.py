"""Level 2: Capture and Sequence Patterns.

Now things get interesting. Commands are split into words, and you'll
match on sequences — destructuring them to extract the parts you need.

This is where "switch thinking" BREAKS. A switch statement matches on
a single value. Pattern matching DESTRUCTURES sequences — it's
generalized iterable unpacking.

Your task: Replace each TODO line with the correct case pattern.
"""

from adventure.handlers_level1 import handle_command as level1_handle


def handle_command(player, words: list[str]) -> str:
    """Handle a multi-word command using capture and sequence patterns."""
    # Delegate single-word commands to Level 1
    if len(words) == 1:
        result = level1_handle(player, words[0])
        if "don't understand" not in result.lower():
            return result

    match words:
        case ["go", direction]:
            if direction in player.current_room.exits:
                player.current_room = player.current_room.exits[direction]
                return player.current_room.look()
            return f"You can't go {direction}."

        # TODO: Add a case for ["take", item_name]
        # HINT: Check if the player already has the item.
        #       If not, find it in the room, remove it, add to inventory.
        #       Pattern: case ["take", item_name]:

        # TODO: Add a case for ["examine", target]
        # HINT: Search room items and player inventory for a match.
        #       Pattern: case ["examine", target]:

        case _:
            return "I don't understand that command."
