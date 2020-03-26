from ucu_students import Student

max = Student("Maxym", "Kuzyshyn", 89, 93)
vova = Student("Volodumyr", "Fedyniak", 95, 100)
jarema = Student("Jarema", "Mischenko", 85, 90)
bogdan = Student("Bogdan", "Vey", 95, 86)

assert isinstance(max, Student)
assert max.get_avg_programming() == 91

assert Student.programming.best == ['Volodumyr Fedyniak', 'Bogdan Vey']
assert Student.calculus.best == ['Maxym Kuzyshyn', 'Volodumyr Fedyniak',
                                 'Jarema Mischenko']