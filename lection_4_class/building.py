import classroom


class AcademicBuilding:
    """Represents an building"""
    def __init__(self, address, classrooms):
        """Initialize"""
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
