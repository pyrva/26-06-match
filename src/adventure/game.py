"""Text adventure game model — Rooms, Items, Player, and game setup."""

from __future__ import annotations


class Item:
    """An item that can be found in rooms and picked up by the player."""

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    def __repr__(self) -> str:
        return f"Item({self.name!r})"


class Room:
    """A room in the text adventure, with exits to other rooms and items to find."""

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description
        self.exits: dict[str, Room] = {}
        self.items: list[Item] = []

    def add_exit(self, direction: str, room: Room) -> None:
        """Add a one-way exit from this room in the given direction."""
        self.exits[direction] = room

    def add_item(self, item: Item) -> None:
        """Place an item in this room."""
        self.items.append(item)

    def remove_item(self, item: Item) -> None:
        """Remove an item from this room (e.g., when picked up)."""
        self.items.remove(item)

    def look(self) -> str:
        """Return a description of the room, its exits, and visible items."""
        lines = [f"You are in the {self.name}.", self.description]

        if self.items:
            item_names = ", ".join(item.name for item in self.items)
            lines.append(f"You see: {item_names}")

        if self.exits:
            exit_list = ", ".join(self.exits.keys())
            lines.append(f"Exits: {exit_list}")

        return "\n".join(lines)

    def __repr__(self) -> str:
        return f"Room({self.name!r})"


class Player:
    """The player character, with a current location and inventory."""

    def __init__(self, current_room: Room) -> None:
        self.current_room = current_room
        self.inventory: list[Item] = []
        self.running = True

    def has_item(self, name: str) -> bool:
        """Check if the player has an item with the given name."""
        return any(item.name == name for item in self.inventory)

    def add_to_inventory(self, item: Item) -> None:
        """Add an item to the player's inventory."""
        self.inventory.append(item)

    def show_inventory(self) -> str:
        """Return a description of the player's inventory."""
        if not self.inventory:
            return "You are carrying nothing."
        item_list = ", ".join(item.name for item in self.inventory)
        return f"You are carrying: {item_list}"

    def move(self, direction: str) -> bool:
        """Move in a direction if there's an exit that way.

        Returns True if the player moved; False if there is no exit in that
        direction (in which case the player stays put).
        """
        if direction in self.current_room.exits:
            self.current_room = self.current_room.exits[direction]
            return True
        return False


# ---------------------------------------------------------------------------
# Game world construction
# ---------------------------------------------------------------------------


def create_game() -> Player:
    """Create the text adventure world and return the player.

    The world has:
    - An entrance hall with exits north and east
    - A library to the north (contains an old book)
    - A kitchen to the east (contains a rusty key and a golden apple)
    - A garden south of the kitchen (contains a wooden sword)

    Directions: north/south/east/west
    """
    entrance = Room("entrance hall", "A grand foyer with marble floors.")
    library = Room("library", "Dusty shelves line the walls, filled with ancient tomes.")
    kitchen = Room("kitchen", "A cozy kitchen with a bubbling pot on the stove.")
    garden = Room("garden", "A sunlit garden with overgrown hedges and a stone bench.")

    # Two-way connections
    entrance.add_exit("north", library)
    library.add_exit("south", entrance)
    entrance.add_exit("east", kitchen)
    kitchen.add_exit("west", entrance)
    kitchen.add_exit("south", garden)
    garden.add_exit("north", kitchen)

    # Items
    library.add_item(Item("book", "A leather-bound book with strange symbols on the cover."))
    kitchen.add_item(Item("key", "A rusty iron key. It looks like it hasn't been used in years."))
    kitchen.add_item(Item("apple", "A golden apple that gleams in the light."))
    garden.add_item(Item("sword", "A wooden training sword, well-worn but sturdy."))

    return Player(current_room=entrance)


def run_command(player: Player, command: str, handler_module: str = "handlers_level1") -> str:
    """Parse and execute a command using the specified handler module.

    This is the main entry point for the game loop. It delegates to the
    appropriate handler based on which exercise level is active.
    """
    from adventure import handlers_complete

    words = command.strip().split()
    if not words:
        return ""

    # Use the complete handlers for the runnable game
    return handlers_complete.handle_command(player, words)
