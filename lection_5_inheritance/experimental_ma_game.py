class Player:
    def __init__(self, current_room):
        self.hunger = 100
        self.money = 1000
        self.health = 100
        self.backpack = []
        self.dead = False
        self.current_room = current_room


class Character:
    def __init__(self, name, description, talk, weakness):
        self.name = name
        self.description = description
        self.talk = talk
        self.weakness = weakness


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def describe(self):
        """ Describes an item"""
        print(f"The [{self.name}] is here - {self.description}")

    def get_name(self):
        return self.name


class Location:
    def __init__(self, name, description, item, character, eating_price=None):
        self.name = name
        self.__description = description
        self.items = None
        self.__directions = None
        self.eating_price = eating_price
        self.__item = item
        self.__character = None

    def make_directions(self, directions):
        """ Creates a dict of all directions"""
        self.__directions = dict(directions)

    def get_details(self):
        """ Prints all the info about a room"""
        print(f"{self.name}\n--------------------\n{self.__description}")
        for i in self.__directions.keys():
            print(f"The {self.__directions[i].name} is {i}")
        if self.__character:
            print(f"{self.__character.name} is here!")

    def get_item(self):
        return self.__item

    def set_item(self, item):
        self.__item = item

    def get_character(self):
        return self.__character

    def move(self, command):
        """ Sets a new room"""
        if command in self.__directions.keys():
            return self.__directions[command]
        else:
            print("There is no room in that direction!")
            return self
