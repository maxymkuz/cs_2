from experimental_ma_game import Player, Location, Item, Character

print("""Hello and welcome to my game. You have to navigate through Lviv
to get from your current location(UCU philosophy department in Sychiv district)
to your home, which is located at Kleparivska street.
 
You start a game with 1000UAH and 100% hunger and health level
YOU WILL DIE IF HUNGER/HEALTH LEVEL DROP TO 0!!!""")

# ITEMS
baseball_bat = Item("Baseball bat", "Usual baseball bat, useful when you want to beat"
                                    " somebody who is not very strong")

whiskey_bottle = Item("Bottle of whiskey", "A bottle of finest Scottish whiskey. "
                                           "Useful for characters like Andriy Sultanov")  # TODO

pack_of_cigarettes = Item("Pack of cigarettes", "Good ukrainian cigarette pack 'Parlament'."
                                                " Useful for americans or other foreigners"
                                                " that are smoking")

kinder_surprise = Item("Kinder-surprise", "Usual kinder-surprise from the nearest shop. "
                                          "Is liked particularly by children.")
# CHARACTERS
mathew = Character("Mathew", "Teacher from America. Used to smoke 30 cigarettes per day "
                             "but now has problems finding them in shops. That is why"
                             "now he is ANGRY at everyone.", "Hey there you dumb", pack_of_cigarettes)
# LOCATIONS
ucu_hutorivka = Location("UCU philosophy department, Hutorivka 35a",
                         "Your starting point. Here is the TRAPEZNA, where you"
                         " can eat, price = 80UAH", pack_of_cigarettes, None, 80)

sykhivsky = Location("Sykhivsky district",
                     "Not well discovered and tricky path. Easy to get lost"
                     " and equally easy to get robbed.\n However the fastest and"
                     " cheapest path so far", whiskey_bottle, None)

ucu_kozelnytska = Location("UCU campus, Kozelnytska 7",
                           "Campus where apps students are studying."
                           "There is a Trapezna here, where you can eat, price = 100UAH",
                           kinder_surprise, mathew, 100)

ucu_hutorivka.make_directions([("east", sykhivsky), ("west", ucu_kozelnytska)])
sykhivsky.make_directions([("west", ucu_hutorivka)])
ucu_kozelnytska.make_directions([("east", ucu_hutorivka)])


player = Player(ucu_hutorivka)

while not player.dead:
    print("\n")
    player.current_room.get_details()

    inhabitant = player.current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = player.current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        # Move in the given direction
        player.current_room = player.current_room.move(command)
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None:
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()

            # Do I have this item?
            if fight_with in player.backpack:
                if inhabitant.fight(fight_with) == True:
                    # What happens if you win?
                    print("Hooray, you won the fight!")
                    player.current_room.character = None
                    if inhabitant.get_defeated() == 2:
                        print("Congratulations, you have vanquished the enemy horde!")
                        dead = True
                else:
                    # What happens if you lose?
                    print("Oh dear, you lost the fight.")
                    print("That's the end of the game")
                    dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            player.backpack.append(item.get_name())
            player.current_room.set_item(None)
        else:
            print("There's nothing here to take!")
    else:
        print("I don't know how to " + command)