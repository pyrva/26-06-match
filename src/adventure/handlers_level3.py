"""Level 3: OR Patterns and Guards.

Now you'll add command aliases and conditional logic INSIDE the match block.

OR patterns let you match multiple alternatives in one case:
    case ["go", ("north" | "n" | "North") as direction]:

Guards add a boolean condition AFTER the pattern:
    case ["go", direction] if direction in player.current_room.exits:

A switch statement can match multiple values with fall-through, but it
CANNOT add conditional logic. This is another level beyond switching.

Your task: Replace each TODO line with the correct case patterns.

New capabilities:
    - Direction abbreviations: "n" → "north", "s" → "south", etc.
    - Command synonyms: "get"/"take"/"grab" all work the same
    - Exit validation: guards check if the direction actually exists
    - Invalid direction feedback: specific message for bad directions
"""

from adventure.handlers_level1 import handle_command as level1_handle


def handle_command(player, words: list[str]) -> str:
    """Handle commands with OR patterns and guards.

    Args:
        player: The Player object.
        words: Command split into words, e.g. ["go", "n"].

    Returns:
        A string response to display to the player.
    """
    # Delegate single-word commands to Level 1
    if len(words) == 1:
        result = level1_handle(player, words[0])
        if "don't understand" not in result.lower():
            return result

    # TODO: Replace the pass statement below with a match/case block that uses:
    #
    # 1. OR patterns with `as` for direction aliases:
    #    case ["go", ("north" | "n") as direction]:
    #    case ["go", ("south" | "s") as direction]:
    #    case ["go", ("east" | "e") as direction]:
    #    case ["go", ("west" | "w") as direction]:

    # 2. A guarded case for any valid exit direction:
    #    case ["go", direction] if direction in player.current_room.exits:

    # 3. A catch-all for invalid directions:
    #    case ["go", _]:

    # 4. OR patterns for command synonyms:
    #    case ["get" | "take" | "grab", item_name]:  →  return player.take(item_name)

    # 5. Examine (same as Level 2) and a wildcard default:
    #    case ["examine", target]:  →  return player.examine(target)
    #    case _:                    →  return "I don't understand that command."

    # HINT: Order matters! Put specific patterns before general ones.
    #       The OR-pattern direction cases should come before the
    #       guarded general-direction case.

    # For direction aliases: normalize them — "n" should become "north"
    # for the actual movement. The match gives you the alias, so map it, then
    # move the player:
    #   direction_map = {"n": "north", "s": "south", "e": "east", "w": "west"}
    #   actual = direction_map.get(direction, direction)
    #   player.move(actual)
    #   return player.current_room.look()
    pass
