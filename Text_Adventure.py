# Simple text adventure with lists only

rooms = [
    "Entrance Hall",  # 0
    "Library",        # 1
    "Kitchen",        # 2
    "Garden",         # 3
    "Puzzle Room",    # 4
    "Tower",          # 5
    "Dungeon",        # 6
    "Armory",         # 7
    "Balcony",        # 8
    "Crypt",          # 9
    "Study"           # 10
]

import random
dungeon_lit = False

# map_links[room] = [north, south, east, west]
# map_links[room] = [north, south, east, west]
map_links = [
    [1, None, None, None],      # 0 Entrance
    [10, 0, 2, None],           # 1 Library (north Study)
    [3, None, None, 1],         # 2 Kitchen
    [5, 2, 4, None],            # 3 Garden
    [None, None, None, 3],      # 4 Puzzle
    [6, 3, 7, 8],               # 5 Tower (north Dungeon, south Garden, east Armory, west Balcony)
    [None, 5, 9, None],         # 6 Dungeon (south Tower, east Crypt)
    [None, None, None, 5],      # 7 Armory (west Tower)
    [None, None, 5, None],      # 8 Balcony (east Tower)
    [None, None, None, 6],      # 9 Crypt (west Dungeon)
    [None, 1, None, None]       # 10 Study (south Library)
]

items = ["key", "lemon", "lantern", "sword"]
item_locations = [9, 2, 10, 7]  # key in Entrance, lemon in Kitchen, lantern in Study, sword in armory


player_room = 0
inventory = []

def show_room():
    print(f"\nYou are in the {rooms[player_room]}")
    if player_room == 0:
        print("The large wooden doors behind you are sealed shut.")
    elif player_room == 1:
        print("Dusty books line the shelves of the Library.")
    elif player_room == 2:
        if "lemon" not in inventory and item_locations[items.index("lemon")] == player_room:
            print("Theres not much in food left in the kitchen, and most of what is there is rotten. You could only find one non-rotten fruit.")
        else:
            print("Theres no edible food left in the kitchen, all of what is there is rotten.")
    elif player_room == 3:
        print("A fountain trickles in the Garden.")
    elif player_room == 4:
        print("There is a locked chest here. you need a key to open it.")
    elif player_room == 5:
        print("You are high in the Tower.")
    elif player_room == 6:
        print("The Dungeon is dark and damp. You hear a strange noise. You might be able to see what's here if you had some light.")
    elif player_room == 7:
        if "sword" not in inventory and item_locations[items.index("sword")] == player_room:
            print("The Armory is lined with old weapons. A sword gleams on a rack.")
        else:
            print("The Armory is lined with old weapons. One of the racks is now empty.")
    elif player_room == 8:
        print("The Balcony overlooks the land. Wind whistles around you.")
    elif player_room == 9:
        print("The Crypt smells of dust and old bones. You would rather be anywhere but here.")
    elif player_room == 10:  # Study
        if "lantern" not in inventory and item_locations[items.index("lantern")] == player_room:
            print("The Study glows with a single lantern's light. A stack of books lays on the desk, dusty and old. You can't read the language they are written in.")
        else:
            print("The Study is now dark and eerie without the light of the lantern. You don't want to stay here any longer.")

    # show items
    for i in range(len(items)):
        if item_locations[i] == player_room:
            print(f"You see a {items[i]} here.")
    # show exits
    dirs = ["north","south","east","west"]
    exits = []
    for d in range(4):
        if map_links[player_room][d] is not None:
            exits.append(f"{dirs[d]} -> {rooms[map_links[player_room][d]]}")
    print("Exits:", ", ".join(exits) if exits else "none")


def move_player(direction):
    global player_room
    dirs = ["north", "south", "east", "west"]
    if direction in dirs:
        idx = dirs.index(direction)
        next_room = map_links[player_room][idx]
        if next_room is not None:
            player_room = next_room
            print(f"You go {direction}.")
        else:
            print("You can't go that way.")
    else:
        print("Invalid direction.")

def take_item(item):
    for i in range(len(items)):
        if items[i] == item and item_locations[i] == player_room:
            inventory.append(item)
            item_locations[i] = None
            print(f"You take the {item}.")
            return
    print("No such item here.")

def use_item(item):
    if item in inventory and player_room == 4 and item == "key":
        print("You unlock a chest with a math puzzle!")
        # generate two random numbers and an operator
        a = random.randint(1, 12)
        b = random.randint(1, 12)
        op = random.choice(["+", "-", "*"])
        if op == "+":
            correct = a + b
        elif op == "-":
            correct = a - b
        else:
            correct = a * b
        ans = input(f"What is {a} {op} {b}? ")
        if ans.strip() == str(correct):
            print("You solved the puzzle and win the treasure inside!")
            return True
        else:
            print("Wrong answer. Try again.")
    elif item in inventory and item == "lemon":
        print("You eat the Lemon. You feel your face pucker up from the sourness.")
        inventory.remove("lemon")
    elif item in inventory and item == "lantern" and player_room == 6:
        print("You light the Dungeon with the lantern. Shadows retreat, but Yzzom the evil Multipoo is revealed! You must defeat him!")
        dungeon_lit = True
        if dungeon_lit and "sword" not in inventory:
            print("But you were unarmed! Yzzom attacks and you are defeated. Game over.")
            exit()
    elif item in inventory and item == "sword" and player_room == 6:
        print("You defeat Yzzom the evil Multipoo! Victory is yours, aswell as the treasure that he was hiding!")
        return True
    else:
        print("You don't see any reason in using that here.")
    return False

def handle_command(cmd):
    parts = cmd.lower().split()
    if len(parts) == 0:
        return False
    if parts[0] in ["north","south","east","west"]:
        move_player(parts[0])
    elif parts[0] == "look":
        show_room()
    elif parts[0] == "take" and len(parts) > 1:
        take_item(parts[1])
    elif parts[0] == "use" and len(parts) > 1:
        return use_item(parts[1])
    elif parts[0] == "inventory":
        print("You have:", inventory if inventory else "nothing")
    else:
        print("Unknown command.")
    return False

# main loop
print("""Welcome Adventurer! The year is 2000, you were lost a bet to your friends and now you have to go into the abandoned castle on the hill that has been there since before you were born. You tried to get out of it but they forced you to into the abandoned fortess and won't let you out untill dawn. You decided that since you're here, that you might as well look around. Who knows, maybe you'll find treasure!

Type 'look' to see your surroundings. type the direction(north, south, east, and west) that you want to go to. use 'take' to pick up items, if there are any. Type 'inventory' to look at what items you have. Type use '(item name)' to use a
item. And finally, type 'exit' if you wish to leave. And make sure to only type in lowercase, or the command won't work! And most importantly, have fun!""")

show_room()
while True:
    cmd = input("> ")
    if cmd.lower() in ["quit","exit"]:
        print("See you next time!")
        break
    if handle_command(cmd):
        break
