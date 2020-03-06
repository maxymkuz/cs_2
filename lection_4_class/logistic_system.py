orderId = 111111


class Item:
    """ Represents and Item with it's price and name"""
    def __init__(self, name, price):
        """ Initializes an Item"""
        self.name = name
        self.price = price

    def __str__(self):
        """ Prints an item in an user-friendly way"""
        return f"{self.name}, PRICE: {self.price}"


class Vehicle:
    """ Represents an Vehicle with unique ID and availability"""
    def __init__(self, id):
        """ Initializes an vehicle"""
        self.isAvailable = True
        self.id = id


class Location:
    """ Represents a Location that has City and it's postal office"""
    def __init__(self, city, postoffice):
        """ Initializes"""
        self.city = city
        self.postoffice = postoffice


class Order:
    """ Represents an Order that inputs all information nessesary
    and creates item list and location instances, assigns vehicles"""
    def __init__(self, user_name="", city='', postoffice=None, items=[]):
        """ Initializes an Order"""
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
        """ (Order, Vehicle) -> None
        Assigns this vehicle to an order"""
        self.vehicle = vehicle.id

    def __str__(self):
        """ Prints order object in useful for user way"""
        return f"Your order {self.orderId} is sent to {self.location.city}." \
               f" Total price: {self.calculate_amount()} UAH."


class LogisticSystem:
    """ Represents an Logistic System, which can place
    a new order and put them in list, also can track
    orders and print tracking in user-friendly way"""
    def __init__(self, vehicles):
        """ Initialize an system"""
        self.orders = []
        self.vehicles = vehicles

    def placeOrder(self, order):
        """ (LogisticSystem, Order) -> None
        Places an order, and checks if there is a vehicle
        available to deliever it and assigns
        a vehicle to a newly created order, else prints that
        all vehicles are occupied"""
        if not all((order.user_name, order.location.city,
                    order.location.postoffice, order.items)):
            print("This order is missing important required arguments"
                  "so it is dismissed, please reorder")
        else:
            if not any([vehicle.isAvailable for vehicle in self.vehicles]):
                print("There is no available vehicle to deliver an order.")
            else:
                for vehicle in self.vehicles:
                    if vehicle.isAvailable:
                        order.vehicle = vehicle.id
                        self.orders.append(order)
                        vehicle.isAvailable = False
                        print("Your order is placed")
                        break

    def trackOrder(self, order_num):
        """ (LogisticSystem, Order) -> None
        Allows to track your orders and prints an order to user"""
        orders = [ord for ord in self.orders if ord.orderId == order_num]
        print("There is no such order") if len(orders) == 0 else print(orders[0])
