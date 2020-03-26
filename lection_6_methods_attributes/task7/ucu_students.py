class Subject:
    """
    This module helps teachers see the top, all and average grades
    of different students in their faculty
    """
    def __init__(self):
        self.lst_of_students = []

    @staticmethod
    def convert_to_american(grade):
        """
        Converts the grade into american system with letters
        :param grade: int
        :return: str
        """
        if grade >= 90:
            return 'A'
        if grade >= 82:
            return 'B'
        if grade >= 70:
            return 'C'
        return 'D' if grade >= 60 else 'F'

    @classmethod
    def best_students(cls, students):
        """
        Returns a list of all students, whose grade from ths subject
        is the 'A' in American system of grading
        :return: lst
        """
        res = [f"{student[0].name} {student[0].surname}" for student in
               students
               if cls.convert_to_american(student[1]) == 'A']
        return res


class Programming(Subject):
    """ Represents an programming course in a University
    """
    avg_grade = 0

    def __init__(self):
        super().__init__()
        self.name = "Programming"

    @classmethod
    def get_avg_grade(cls):
        return cls.avg_grade

    def add_student(self, student):
        """
        Adds a students and sets a new average grade
        for Programming
        :param student:
        :return: None
        """

        self.lst_of_students.append(student)
        Programming.avg_grade = sum([i.programming_grade for i in
                              self.lst_of_students]) / len(
            self.lst_of_students)

    @property
    def best(self):
        """ Property that returns the best students by grade"""
        return Subject.best_students([(i, i.programming_grade) for i
                                            in self.lst_of_students])


class Calculus(Subject):
    """ Represents an Calculus course in a University
    """

    avg_grade = 0

    def __init__(self):
        super().__init__()
        self.name = "Calculus"

    def add_student(self, student):
        """
        Adds a students and sets a new average grade for
        Calculus
        :param student:
        :return: None
        """

        self.lst_of_students.append(student)
        Calculus.avg_grade = sum([i.calculus_grade for i in
                              self.lst_of_students]) / len(
            self.lst_of_students)

    @classmethod
    def get_avg_grade(cls):
        return cls.avg_grade

    @property
    def best(self):
        return Subject.best_students([(i, i.calculus_grade) for i
                                            in self.lst_of_students])

class Student:
    programming = Programming()
    calculus = Calculus()

    def __init__(self, name, surname, programming_grade, calculus_grade):
        self.name = name
        self.surname = surname
        self.programming_grade = programming_grade
        self.calculus_grade = calculus_grade
        Student.programming.add_student(self)
        Student.calculus.add_student(self)

    @classmethod
    def get_avg_programming(cls):
        return Programming.avg_grade

    @classmethod
    def get_avg_calculus(cls):
        return Calculus.avg_grade
