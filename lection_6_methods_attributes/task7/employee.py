import datetime


class Employee:
    """
    An class to represent a single empoyee
    in a company. Useful for managers
    """
    all_employees = []
    total_amount = 0
    bonus = 1

    def __init__(self, name, surname, salary):
        self.first = name
        self.last = surname
        self.salary = salary
        Employee.all_employees.append(self)
        Employee.total_amount += 1

    def raise_bonus(self):
        """
        Make bonuses true
        :return:
        """
        self.salary = int(self.salary * Employee.bonus)

    @classmethod
    def make_new_bonus(cls, amount):
        """
        Sets a new bonus amount
        """
        cls.bonus = amount

    @staticmethod
    def is_workday(day):
        """ Returns true if it's workday
        """
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    @property
    def get_employees(self):
        return Employee.all_employees

