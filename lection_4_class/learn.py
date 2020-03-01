class Student:
    classes_taken = 6

    def __init__(self, name):
        self.name = name


Student.classes_taken = 81

me = Student("Max")
me.classes_taken = 81
print(me.__dict__)
