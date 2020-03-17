class Bird:
    """ Represents a usual bird"""
    def __init__(self, name):
        self.name = name
        self.num_of_eggs = 0
        self.can_fly = True
        self.can_swim = False

    def fly(self):
        return "I can fly!" if self.can_fly else "No flying for me."

    def layEgg(self):
        self.num_of_eggs += 1

    def countEggs(self):
        return self.num_of_eggs

    def __repr__(self):
        egg_s = "egg" if self.num_of_eggs == 1 else "eggs"
        return f"{self.name} has {self.num_of_eggs} {egg_s}"


class Penguin(Bird):
    def fly(self):
        return "No flying for me."

    def swim(self):
        return "I can swim!"


class MessengerBird(Bird):
    def __init__(self, name, message=""):
        super().__init__(name)
        self.message = message

    def deliverMessage(self):
        return self.message