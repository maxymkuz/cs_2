from task6.realestate import *


def realestate_testing():
    """
       By the way, there is no point in making get_valid_input a static
    or class method because it doesn't use any class variables
    and has nothing to do with a lot of classes that inherit
    Property or Apartment or any other class
        In this module, staticmethod is used in each class, but for
    the same purpose -- to call the promt_init method(which is also
    static) from the parent class or classes if there exist(s) such
    and fill the parent_init dictionary with the information, needed
    for a parent class. Then this dictionary get's updated on the
    current class requirements and add the information needed for
    this class, after which this static method returns this dictionary
    :return: None
    """
    print("Testing the reaestate... ", end="")
    agent = Agent()
    assert isinstance(agent, Agent)

    assert agent.property_list == []

    assert issubclass(HousePurchase, Purchase)
    assert issubclass(HousePurchase, House)

    assert issubclass(ApartmentRental, Rental)
    assert issubclass(ApartmentRental, Apartment)
    assert "prompt_init" in ApartmentRental.__dict__
    assert type(ApartmentRental.__dict__["prompt_init"]) == staticmethod

    rental = ApartmentRental("yes", 1000, "None")

    assert rental.furnished == "yes"
    assert rental.rent == 1000

    purchase = Purchase(110, 1000)

    assert rental.price == 110
    assert rental.rent == 1000
    assert "prompt_init" in purchase.__dict__
    assert type(purchase.__dict__["prompt_init"]) == staticmethod

    apartment = Apartment()
    assert apartment.balcony == ""
    assert apartment.valid_laundries == ("coin", "ensuite", "none")

    assert issubclass(Apartment, Property)
    assert issubclass(House, Property)
    property = Property('11', '2')

    assert property.square_feet == '11'
    assert property.num_baths == ''
    assert "prompt_init" in property.__dict__
    assert type(property.__dict__["prompt_init"]) == staticmethod
    print("The testing is done successfully")
