"""Level 4: Class Patterns.

This is where "switch thinking" becomes IMPOSSIBLE.
"""

from adventure.events import Click, KeyPress, Quit, TextCommand
from adventure.handlers_level3 import handle_command as level3_handle

WASD_MAP = {"w": "north", "a": "west", "s": "south", "d": "east"}


def handle_event(player, event) -> str:
    """Handle a game event using class patterns."""
    match event:
        # Click event — extract position coordinates
        case Click((x, y)):
            if (x, y) == (0, 0):
                return "Nothing interesting there."
            return f"You click at position ({x}, {y})."

        # Quit with OR pattern for both cases
        case KeyPress("q") | KeyPress("Q"):
            player.running = False
            return "Goodbye!"

        # TODO: Add a guarded case for WASD movement
        # HINT: case KeyPress(key) if key in WASD_MAP:
        #       Delegate to level3: level3_handle(player, ["go", WASD_MAP[key]])

        # TODO: Add a case for unknown keys
        # HINT: case KeyPress(key):

        # TODO: Add a case for TextCommand
        # HINT: case TextCommand(text):
        #       words = text.strip().split()
        #       return level3_handle(player, words)

        # TODO: Add a case for Quit event
        # HINT: case Quit():

        case _:
            return "Unknown event."
