class Classroom:
    """Represents an classroom"""
    def __init__(self, number, capacity, equipment):
        """Initialize"""
        self.number = number
        self.capacity = capacity
        self.equipment = equipment

    def __str__(self):
        """ (Student) -> str
        Return the string representation of the student"""
        return f"Classroom {self.number} has a capacity of {self.capacity}\
 persons and has the following equipment: {', '.join(self.equipment)}."

    def is_larger(self, other):
        """ (Classroom, Classroom) -> bool
        Ret True if larger"""
        return self.capacity > other.capacity

    def equipment_differences(self, other):
        """ (Classroom, Classroom) -> list
        Returns the difference in equipments"""
        return [i for i in self.equipment if i not in other.equipment]

    def __repr__(self):
        """For debugging and other developers"""
        return f"Classroom('016', 80, ['PC', 'projector', 'mic'])"


classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
classroom_007 = Classroom('007', 12, ['TV'])

