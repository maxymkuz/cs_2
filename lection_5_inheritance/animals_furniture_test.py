from animals_furniture import Animal, Cat, Furniture, Chair

if __name__ == '__main__':
    furniture1 = Furniture("empire", "bedroom")

    furniture2 = Furniture("modern", "bathroom")
    assert (not (furniture1 == furniture2))

    assert (furniture1.style == "empire")
    assert (furniture1.assign == "bedroom")

    assert (str(furniture1) == "<furniture style is empire>")

    chair1 = Chair("empire", "bedroom", "armchair")
    chair1 = Chair("empire", "bedroom", "armchair")

    assert (chair1.tipe == "armchair")
    assert (isinstance(chair1, Furniture))

    assert (str(chair1) == "<This armchair furniture style is empire>")

    assert (chair1.get_assign() == "bedroom")
    animal1 = Animal("chordata", "mammalia")
    assert(animal1.phylum == "chordata")
    assert(animal1.clas == "mammalia")
    assert(str(animal1) == "<animal class is mammalia>")
    animal2 = Animal("chordata", "birds")
    assert(not (animal1 == animal2))
    cat1 = Cat("chordata", "mammalia", "felis")
    assert(cat1.sound() == "Meow")
    assert(cat1.genus == "felis")
    assert(isinstance(cat1, Animal))
    assert(str(cat1) == "<This felis animal class is mammalia>")
