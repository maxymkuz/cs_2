class Animal:
    """
    Represents an animal class
    """
    def __init__(self, phylum, clas):
        """ Initializes an instance of animal"""
        self.phylum = phylum
        self.clas = clas

    def __str__(self):
        """ Prints in an user-friendly way"""
        return f"<animal class is {self.clas}>"


class Cat(Animal):
    """ Represents a cat -- an instance of animal"""
    def __init__(self, phylum, clas, genus=""):
        super().__init__(phylum, clas)
        self.genus = genus

    def sound(self):
        """ Default sound of all cats"""
        return "Meow"

    def __str__(self):
        """ Prints in a user-friendly way"""
        return f"<This {self.genus} animal class is {self.clas}>"


class Furniture:
    """ Represent a big Furniture class"""
    def __init__(self, style, assign):
        self.style = style
        self.assign = assign

    def __str__(self):
        """ Prints in a user-friendly way"""
        return f"<furniture style is {self.style}>"


class Chair(Furniture):
    """ Represents a chair -- an instance of Furniture"""
    def __init__(self, style, assign, tipe):
        super().__init__(style, assign)
        self.tipe = tipe

    def get_assign(self):
        """ Just returns an assign"""
        return self.assign

    def __str__(self):
        """ Prints in a user-friendly way"""
        return f"<This {self.tipe} furniture style is {self.style}>"

print(dir(Chair))