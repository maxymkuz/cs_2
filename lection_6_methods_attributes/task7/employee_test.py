from employee import Employee
import datetime


if __name__ == '__main__':
    num1 = Employee('Maxym', 'Kuzyshyn', 10000)
    num2 = Employee('Volodumyr', 'Fedyniak', 2000)

    Employee.make_new_bonus(1.05)

    assert Employee.bonus == 1.05

    my_date = datetime.date(2020, 2, 4)

    assert Employee.is_workday(my_date)
