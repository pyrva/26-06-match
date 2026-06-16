"""Level 2: Capture and Sequence Patterns.

Now things get interesting. Commands are split into words, and you'll
match on sequences — destructuring them to extract the parts you need.

This is where "switch thinking" BREAKS. A switch statement matches on
a single value. Pattern matching DESTRUCTURES sequences — it's
generalized iterable unpacking.

    command = "go north".split()   →   ["go", "north"]

    match command:
        case ["go", direction]:   # direction captures "north"!
            player.move(direction)

The key insight: `direction` is an ASSIGNMENT TARGET (like in unpacking),
not a comparison. It binds a new variable.

Your task: Replace each TODO line with the correct case pattern.

Available commands (input is already split into a list of words):
    - ["go", direction]   → Move in the given direction
    - ["take", item]      → Pick up an item
    - ["examine", target] → Look at an item or feature
    - Single-word commands from Level 1 still work (delegate to level1)
    - anything else       → "I don't understand that command."
"""

from adventure.handlers_level1 import handle_command as level1_handle


def handle_command(player, words: list[str]) -> str:
    """Handle a multi-word command using capture and sequence patterns.

    Args:
        player: The Player object.
        words: Command split into words, e.g. ["go", "north"].

    Returns:
        A string response to display to the player.
    """
    # First, handle single-word commands by delegating to Level 1.
    # If the Level 1 handler returns something other than the wildcard
    # response, return it. Otherwise, fall through to the multi-word cases.
    if len(words) == 1:
        result = level1_handle(player, words[0])
        if "don't understand" not in result.lower():
            return result

    # TODO: Replace the pass statement below with a match/case block
    # that handles multi-word commands using capture and sequence patterns.

    # HINT: Use `match words:` with patterns like:
    #   case ["go", direction]:      → move the player
    #   case ["take", item_name]:    → pick up an item from the room
    #   case ["examine", target]:    → describe an item or feature
    #   case _:                      → catch-all for unknown commands

    # For ["go", direction]:
    #   player.move(direction) moves the player and returns True if it worked
    #   (False if there's no exit that way).
    #   If it moved: return the new room's description via player.current_room.look()
    #   If not: return f"You can't go {direction}."

    # For ["take", item_name]:
    #   player.take(item_name) does it all — checks your inventory, finds the
    #   item in the room, moves it, and returns the right message. Just return it.

    # For ["examine", target]:
    #   player.examine(target) searches the room then your inventory and returns
    #   the item's description (or "You don't see {target} here."). Just return it.

    # Remember: capture patterns BIND variables — they don't compare them!
    # case ["go", direction]: means "match a 2-element list starting with 'go'
    # and bind the second element to the variable 'direction'."
    pass
