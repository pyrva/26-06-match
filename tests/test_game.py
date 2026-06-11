"""Tests for the game model — rooms, items, player, and world setup."""

from adventure.game import Item, Player, Room, create_game


class TestItem:
    def test_item_has_name_and_description(self):
        item = Item("sword", "A sharp blade.")
        assert item.name == "sword"
        assert item.description == "A sharp blade."

    def test_item_repr(self):
        item = Item("key", "A rusty key.")
        assert repr(item) == "Item('key')"


class TestRoom:
    def test_room_has_name_and_description(self):
        room = Room("library", "Dusty shelves.")
        assert room.name == "library"
        assert room.description == "Dusty shelves."

    def test_room_starts_with_no_exits_or_items(self):
        room = Room("cell", "A dark cell.")
        assert room.exits == {}
        assert room.items == []

    def test_add_exit(self):
        hall = Room("hall", "A hall.")
        kitchen = Room("kitchen", "A kitchen.")
        hall.add_exit("north", kitchen)
        assert hall.exits["north"] is kitchen

    def test_add_and_remove_item(self):
        room = Room("room", "A room.")
        sword = Item("sword", "Sharp.")
        room.add_item(sword)
        assert sword in room.items
        room.remove_item(sword)
        assert sword not in room.items

    def test_look_describes_room_exits_and_items(self):
        room = Room("kitchen", "A cozy kitchen.")
        garden = Room("garden", "A garden.")
        room.add_exit("south", garden)
        room.add_item(Item("apple", "A red apple."))
        result = room.look()
        assert "kitchen" in result
        assert "cozy kitchen" in result
        assert "apple" in result
        assert "south" in result


class TestPlayer:
    def test_player_starts_in_room_with_empty_inventory(self):
        room = Room("start", "Starting room.")
        player = Player(room)
        assert player.current_room is room
        assert player.inventory == []
        assert player.running is True

    def test_has_item(self):
        room = Room("room", "A room.")
        player = Player(room)
        player.add_to_inventory(Item("sword", "A sword."))
        assert player.has_item("sword") is True
        assert player.has_item("shield") is False

    def test_show_inventory_empty(self):
        room = Room("room", "A room.")
        player = Player(room)
        assert player.show_inventory() == "You are carrying nothing."

    def test_show_inventory_with_items(self):
        room = Room("room", "A room.")
        player = Player(room)
        player.add_to_inventory(Item("sword", "A sword."))
        player.add_to_inventory(Item("key", "A key."))
        result = player.show_inventory()
        assert "sword" in result
        assert "key" in result


class TestCreateGame:
    def test_player_starts_in_entrance_hall(self):
        player = create_game()
        assert player.current_room.name == "entrance hall"

    def test_entrance_has_north_and_east_exits(self):
        player = create_game()
        exits = player.current_room.exits
        assert "north" in exits
        assert "east" in exits

    def test_library_has_book(self):
        player = create_game()
        library = player.current_room.exits["north"]
        assert any(item.name == "book" for item in library.items)

    def test_kitchen_has_key_and_apple(self):
        player = create_game()
        kitchen = player.current_room.exits["east"]
        item_names = [item.name for item in kitchen.items]
        assert "key" in item_names
        assert "apple" in item_names

    def test_garden_accessible_from_kitchen(self):
        player = create_game()
        kitchen = player.current_room.exits["east"]
        garden = kitchen.exits["south"]
        assert garden.name == "garden"
        assert any(item.name == "sword" for item in garden.items)

    def test_two_way_connections(self):
        player = create_game()
        library = player.current_room.exits["north"]
        assert library.exits["south"] is player.current_room
