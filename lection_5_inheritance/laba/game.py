class Item:
    """ An instance of an Item"""

    def __init__(self, name):
        self.name = name
        self.description = ""

    def set_description(self, description):
        """ Desc. to the item"""
        self.description = description

    def describe(self):
        """ Describes an item"""
        print(f"The [{self.name}] is here - {self.description}")

    def get_name(self):
        return self.name


won_times = 0


class Inhabitant:
    """ An character, could be good and bad"""

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.conversation = ""
        self.defeated = 0

    def set_conversation(self, conversation):
        """ What does the enemy say"""
        self.conversation = conversation

    def talk(self):
        print(f"[{self.name} says]: {self.conversation}")

    def describe(self):
        print(f"{self.description}")

    @staticmethod
    def get_defeated(self):
        global won_times
        won_times += 1
        return won_times


class Enemy(Inhabitant):
    """ Creates an instance of an enemy
    """

    def __init__(self, name, description):
        super().__init__(name, description)
        self.weakness = ""

    def set_weakness(self, weakness):
        """ Sets an weakness of current enemy"""
        self.weakness = weakness

    def fight(self, item):
        """ True if user wins"""
        if self.weakness == item:
            print(f"You fend {self.name} off with the {item}")
            return  True
        return False


class Room:
    """ Creates an instance of
    any of the available rooms"""

    def __init__(self, name):
        self.name = name
        self.description = ""
        self.directions = {}
        self.character = None
        self.item = None

    def set_description(self, description):
        """ Sets description"""
        self.description = description

    def link_room(self, other, direction):
        """ Sets the room direction"""
        self.directions[direction] = other

    def set_character(self, enemy):
        """ Assigns an enemy to """
        self.character = enemy

    def set_item(self, item):
        """ Assigns an item to room"""
        self.item = item

    def get_details(self):
        """ Prints all the info about a room"""
        print(f"{self.name}\n--------------------\n{self.description}")
        for i in self.directions.keys():
            print(f"The {self.directions[i].name} is {i}")
        if self.character:
            print(f"{self.character.name} is here!")

    def get_character(self):
        return self.character

    def get_item(self):
        return self.item

    def move(self, command):
        """ Sets a new room"""
        if command in self.directions.keys():
            return self.directions[command]
        else:
            print("There is no room in that direction!")
            return self
