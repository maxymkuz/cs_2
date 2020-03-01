orderId = 111111


class Item:
    """ Represents and Item"""
    def __init__(self, name, price):
        """ Initializes"""
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}, PRICE: {self.price}"


class Vehicle:
    """ Represents an Vehicle"""
    def __init__(self, id):
        """ Initializes"""
        self.isAvailable = True
        # global vehicle_id
        self.id = id
        # vehicle_id += 1


class Location:
    """ Represents a Location"""
    def __init__(self, city, postoffice):
        """ Initializes"""
        self.city = city
        self.postoffice = postoffice


class Order:
    """ Represents an Order"""
    def __init__(self, user_name="", city='', postoffice=None, items=[]):
        """ Initializes"""
        self.user_name = user_name
        self.location = Location(city, postoffice)
        self.items = items
        global orderId
        self.orderId = orderId
        orderId += 1
        self.vehicle = None
        print(f"Your order number is {self.orderId}.")

    def calculate_amount(self):
        """ (Order) -> int
        Calculates the price of an order"""
        return sum([item.price for item in self.items])

    def assign_vehicle(self, vehicle):
        """ Assigns this vehicle to an order"""
        self.vehicle = vehicle.id

    def __str__(self):
        """ Useful print of this"""
        return f"Your order {self.orderId} is sent to {self.location.city}." \
               f" Total price: {self.calculate_amount()} UAH."


class LogisticSystem:
    """ Represents an Logistic System"""
    def __init__(self, vehicles):
        """ Initialize"""
        self.orders = []
        self.vehicles = vehicles

    def placeOrder(self, order):
        """ Places an order"""
        if not all((order.user_name, order.location.city,
                    order.location.postoffice, order.items)):
            print("This order is missing important required arguments"
                  "so it is dismissed, please reorder")
        else:
            print([vehicle.isAvailable for vehicle in vehicles])
            if not any([vehicle.isAvailable for vehicle in vehicles]):
                print("There is no available vehicle to deliver an order.")
            else:
                for vehicle in self.vehicles:
                    if vehicle.isAvailable:
                        order.vehicle = vehicle.id
                        self.orders.append(order)
                        vehicle.isAvailable = False
                        break

    def trackOrder(self, order_num):
        """ Allows to track your orders"""
        orders = [ord for ord in self.orders if ord.orderId == order_num]
        print("There is no such order") if len(orders) == 0 else print(orders[0])



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