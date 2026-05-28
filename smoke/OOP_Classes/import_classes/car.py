class Car:
    """A simple attempt to present a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""

        self.make = make # attributes
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self): # method
        """Return a formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")


    def update_odometer(self, mileage):  # updates attribute value through method
        """Set the odometer to the given value.
        Reject change if it attempts to roll the odometer back."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("odometer reading roll backs not allowed")

    def increment_odometer(self, miles):
        """Add amount to odometer reading"""
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, batt_size=22): #battery_size is an optional parameter
        """initialize battery's attributes."""
        self.battery_size = batt_size

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery.")


    def get_range(self):
        """Print a statement about the range this battery provides"""

        if self.battery_size < 40:
            srange = 150
        elif self.battery_size > 41:
            srange = 175
        elif self.battery_size > 65:
            srange = 225
        print(f"This car's range is about {srange}")


class ElectricCar(Car): # Child class; Car class referenced in the ()
    """represents aspects of parent class, specific to child class"""

    def __init__(self, make, model, year):
        """
        Initialize attributes of parent class.
        Initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year) #special function that allows to call method from parent class
        # gives child class all attributes from parent class
        self.battery = Battery()  # calls the child class attribute points to the Battery __init__
        #calls the Battery class
