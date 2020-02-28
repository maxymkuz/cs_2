class Classroom:
    def __init__(self, number, capacity, equipment):
        self.number = number
        self.capacity = capacity
        self.equipment = equipment
    def __str__(self):
        return f"Classroom {self.number} has a capacity of {self.capacity}\
 persons and has the following equipment: {', '.join(self.equipment)}."
    def is_larger(self, other):
        return self.capacity > other.capacity
    def equipment_differences(self, other):
        return [i for i in self.equipment if i not in other.equipment]
    def __repr__(self):
        return f"{type(self)}('016', 80, ['PC', 'projector', 'mic'])"


classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
classroom_007 = Classroom('007', 12, ['TV'])
