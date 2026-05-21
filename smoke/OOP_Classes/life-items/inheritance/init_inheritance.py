class Car: # Parent Clas
    """A simple attempt to represent a car."""
    def __init__(self, make , model, year): # parameters
        """Initialize attributes"""
        self.make = make   # attributes
        self.model = model
        self.year = year
        self.odometer_reading = 0 # default attributes

    def get_descriptive_name(self):
        """Return descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def raad_odometer(self):
        """Print car's mileage"""
        print(self.odometer_reading)

    def update_odometer(self, mileage):
        """Set odometer to given value"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Cannot roll back the odometer")

    def increment_odometer(self, miles):
        """Add given amount to odometer"""
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, bat_size): #battery_size is an optional parameter
        """initialize battery's attributes."""
        self.battery_size = bat_size

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

    # def upgrade_batter(self):
    #
    #     if self.battery_size:
    #         pass
    #     else:
    #         self.battery_size == 65

class ElectricCar(Car): # Child class; Car class referenced in the ()
    """represents aspects of parent class, specific to child class"""

    def __init__(self, make, model, year):
        """
        Initialize attributes of parent class.
        Initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year) #special function that allows to call method from parent class
        # gives child class all attributes from parent class
        self.battery = Battery(11)  # calls the child class attribute points to the Battery __init__
        #calls the Battery class



my_leaf = ElectricCar('nissan', 'leaf', 2024) # instantiation of the class ElectricCar
print(my_leaf.get_descriptive_name())

my_syrus = ElectricCar('toyota', 'syrus', 2022)
print(my_syrus.get_descriptive_name())


#.battery = creates a new instance from the class battery
my_leaf.battery.get_range()
