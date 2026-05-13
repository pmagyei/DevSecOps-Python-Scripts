class Car:
    """A simple attempt to present a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""

        self.make = make # attributes
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self): # method
        """Return formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def update_odometer(self, mileage):  #updates attribute value through method
        """Set odometer to given value.
        Reject change if it attempts to roll the odometer back."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("odometer reading roll backs not allowed")
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")


my_new_car = Car("audi", "a4", 2024) # instance from the class
print(my_new_car.get_descriptive_name())

#my_new_car.update_odometer(25) # updates the attribute though the method

#my_new_car.odometer_reading = 23 # directly access the attributes
my_new_car.read_odometer()