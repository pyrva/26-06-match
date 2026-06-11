"""Level 4: Class Patterns.

This is where "switch thinking" becomes IMPOSSIBLE. You're no longer
matching strings or lists — you're matching on the TYPE of an object
and EXTRACTING its attributes in one expression.

    match event:
        case Click((x, y)):          # type check + attribute extraction
        case KeyPress("q") | KeyPress("Q"):  # type + literal attribute
        case KeyPress(key) if key in "wasd": # type + capture + guard
        case TextCommand(text):       # type + capture
        case Quit():                  # type check only

This is "generalized iterable unpacking" applied to objects. The case
pattern Click((x, y)) is like writing:
    if isinstance(event, Click):
        (x, y) = event.position

...but in one expression. That's the power of structural pattern matching.

Your task: Replace each TODO line with the correct case patterns.
"""

from adventure.events import Click, KeyPress, Quit, TextCommand
from adventure.handlers_level3 import handle_command as level3_handle


def handle_event(player, event) -> str:
    """Handle a game event using class patterns.

    Args:
        player: The Player object.
        event: An event object — Click, KeyPress, Quit, or TextCommand.

    Returns:
        A string response to display to the player.
    """
    # TODO: Replace the pass statement below with a match/case block
    # that handles each event type using class patterns.
    #
    # HINT: Use `match event:` with class patterns:
    #
    #   case Click((x, y)):
    #       Return a description of what's at position (x, y) in the room.
    #       For now, just return f"You click at position ({x}, {y})."
    #       If the position is (0, 0): return "Nothing interesting there."
    #
    #   case KeyPress("q") | KeyPress("Q"):
    #       Quit the game: set player.running = False, return "Goodbye!"
    #
    #   case KeyPress(key) if key in "wasd":
    #       WASD movement shortcuts: w=north, a=west, s=south, d=east
    #       Use a dict: wasd = {"w": "north", "a": "west", "s": "south", "d": "east"}
    #       Delegate to the level3 handler: level3_handle(player, ["go", wasd[key]])
    #
    #   case KeyPress(key):
    #       Unknown key: return f"Unknown key: {key}"
    #
    #   case TextCommand(text):
    #       Parse the text as a command and delegate to level3.
    #       words = text.strip().split()
    #       return level3_handle(player, words)
    #
    #   case Quit():
    #       Quit the game: set player.running = False, return "Goodbye!"
    #
    # Remember: class patterns combine isinstance + attribute extraction!
    # case Click((x, y)): checks isinstance(event, Click) AND
    # destructures event.position into (x, y).
    pass
