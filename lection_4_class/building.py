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

classroom_016 = classroom.Classroom('016', 80, ['PC', 'projector', 'mic'])
classroom_007 = classroom.Classroom('007', 12, ['TV'])
classroom_008 = classroom.Classroom('008', 25, ['PC', 'projector'])
classrooms = [classroom_016, classroom_007, classroom_008]

building = AcademicBuilding('Kozelnytska st. 2a', classrooms)

# for room in building.classrooms:
#     print(room)
print(building.total_equipment())
print(building)