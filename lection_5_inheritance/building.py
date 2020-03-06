from classroom import Classroom


class Building:
    """ Represents an usual building."""
    def __init__(self, building, address):
        """ Initializes a building."""
        self.building = building
        self.address = address


class House(Building):
    """ Inherits it's attributes from Building class and represents an concrete building"""
    def __init__(self, building, address, list_of_flats):
        super().__init__(building, address)
        self.address = address


class AcademicBuilding(Building):
    """ Inherits from building, is an academic building."""
    def __init__(self, address, classrooms):
        """Initialize"""
        super().__init__("Academic", address)
        self.address = address
        self.classrooms = classrooms

    def total_equipment(self):
        """ (AcademicBuilding) -> list
        Returns sll the equipment available in equipments"""
        lst = [j for i in self.classrooms for j in i.equipment]
        return list(set([(i, lst.count(i)) for i in lst]))

    def __str__(self):
        """ (AcademicBuilding) -> str
            Return the string representation of the AcademicBuilding"""
        return self.address + '\n' + '\n'.join([i.__str__() for i in self.classrooms])
