"""Level 1: Literal and Wildcard Patterns.

In this level, commands are single words. You'll use literal patterns
to match specific commands and the wildcard pattern `_` to handle
everything else.

This is the ONE level where "switch thinking" works — you're matching
on exact values. Enjoy it while it lasts!

Your task: Replace each TODO line with the correct case pattern.

Available commands:
    - "quit"     → Say goodbye and set player.running = False
    - "look"     → Describe the current room (use player.current_room.look())
    - "help"     → Show available commands
    - "inventory" → Show what the player is carrying (use player.show_inventory())
    - anything else → "I don't understand that command."
"""


def handle_command(player, command: str) -> str:
    """Handle a single-word command using literal and wildcard patterns.

    Args:
        player: The Player object (has current_room, inventory, running).
        command: A single word like "quit", "look", etc.

    Returns:
        A string response to display to the player.
    """
    # TODO: Replace the pass statement below with a match/case block
    # that handles "quit", "look", "help", "inventory", and a wildcard default.
    #
    # HINT: Use `match command:` and literal patterns like `case "quit":`.
    #       Use `case _:` for the default (wildcard) case.
    #
    # For "quit", set player.running = False and return "Goodbye!"
    # For "look", return player.current_room.look()
    # For "help", return the help text shown below
    # For "inventory", return player.show_inventory()
    # For anything else, return "I don't understand that command."
    #
    # Remember: pattern matching is case-sensitive!
    # "LOOK" should NOT match "look" — it should fall to the wildcard.
    pass
