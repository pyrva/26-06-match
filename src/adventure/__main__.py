"""Run the text adventure game with the complete handlers."""

from adventure.game import create_game
from adventure.handlers_complete import handle_command


def main():
    player = create_game()
    print("Welcome to the Pattern Matching Adventure!")
    print("Type 'help' for available commands.\n")
    print(player.current_room.look())

    while player.running:
        try:
            command = input("\n> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not command:
            continue

        words = command.split()
        result = handle_command(player, words)
        print(result)


if __name__ == "__main__":
    main()
