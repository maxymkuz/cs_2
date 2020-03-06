from classroom import Classroom
from building import AcademicBuilding, House, Building


classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
classroom_007 = Classroom('007', 12, ['TV'])
classroom_008 = Classroom('008', 25, ['PC', 'projector'])
classrooms = [classroom_016, classroom_007, classroom_008]
building_2a = AcademicBuilding('Kozelnytska st. 2a', classrooms)
assert isinstance(building_2a, AcademicBuilding)
for room in building_2a.classrooms:
    assert isinstance(room, Classroom)
print("Methods: ", dir(building_2a))
print("Attributes: ", building_2a.__dict__)
print("Equipment", building_2a.total_equipment())
print("There are no errors. Thank You!")