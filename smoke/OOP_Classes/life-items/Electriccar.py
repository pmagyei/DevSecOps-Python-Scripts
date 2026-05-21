class Car:
    """A simple attempt to present a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""

        self.make = make # attributes
        self.model = model
        self.year = year
        self.odometer_reading = 20000

    def get_descriptive_name(self): # method
        """Return a formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def update_odometer(self, mileage):  #updates attribute value through method
        """Set the odometer to the given value.
        Reject change if it attempts to roll the odometer back."""
        #if mileage >= self.odometer_reading:
        self.odometer_reading = mileage
       # else:
            #print ("odometer reading rollbacks not allowed")

    # def increment_odometer(self, miles):
    #     """Add amount to odometer reading"""
    #     self.odometer_reading += miles

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")


ny_used_car = Car("subaru", "outback", 2019)
print(ny_used_car.get_descriptive_name())

ny_used_car.update_odometer(23_500)
ny_used_car.read_odometer()