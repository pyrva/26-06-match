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
    help_text = (
        "Available commands:\n"
        "  look       — look around the room\n"
        "  go <dir>   — move in a direction\n"
        "  take <item>— pick up an item\n"
        "  inventory  — check your inventory\n"
        "  help       — show this help text\n"
        "  quit       — exit the game"
    )

    match command:
        case "quit":
            player.running = False
            return "Goodbye!"
        # TODO: Add cases for "look", "help", "inventory"
        # HINT: These follow the same pattern as "quit" above.
        #       Use player.current_room.look() for "look",
        #       return help_text for "help",
        #       use player.show_inventory() for "inventory".
        # TODO: Add a wildcard case `case _:` for unknown commands.
        #       Return "I don't understand that command."
        case _:
            return "I don't understand that command."
