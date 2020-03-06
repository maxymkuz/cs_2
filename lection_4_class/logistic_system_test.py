from logistic_system import Item, Vehicle, Location, LogisticSystem, Order


if __name__ == '__main__':
    vehicles = [Vehicle(1), Vehicle(2)]
    logSystem = LogisticSystem(vehicles)

    my_items = [Item('book', 110), Item('chupachups', 44)]
    my_order = Order(user_name='Oleg', city='Lviv', postoffice=53, items=my_items)
    logSystem.placeOrder(my_order)

    my_items2 = [Item('flowers', 11), Item('shoes', 153), Item('helicopter', 0.33)]
    my_order2 = Order('Andrii', 'Odessa', 3, my_items2)
    logSystem.placeOrder(my_order2)

    my_items3 = [Item('coat', 61.8), Item('shower', 5070), Item('rollers', 700)]
    my_order3 = Order('Olesya', 'Kharkiv', 17, my_items3)
    logSystem.placeOrder(my_order3)

    assert isinstance(logSystem, LogisticSystem)
    print("There are no errors. Thank You!")