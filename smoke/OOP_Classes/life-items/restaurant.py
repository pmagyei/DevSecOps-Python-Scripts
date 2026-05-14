class Restaurant:
    """Prints and describes"""

    def __init__(self, restaurant_name):
        """initialize attributes to dscribe restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = ""   # default attributes do not need to be defined as parameters
        self.number_served = 0

    def describe_restaurant(self):
        """describe cuisine"""
        print(f"{self.restaurant_name} is a nice restaurant")

    def restaurant_cuisine(self, cuisine):
        """describes cuisine type"""
        self.cuisine_type = cuisine
        print(f"{self.cuisine_type} cuisine is nice")

    def open_restaurant(self):
        """describe's restaurant openings"""
        print(f"{self.restaurant_name} is open everyday until Midnight")

    def customers_served(self, number):
        """outputs numbers of customers served"""
        self.number_served = number # reads attribute, assigns argument to attribute
        print(self.number_served)
    def more_customers(self, more):
        """increase the amount of customers served"""
        self.number_served += more
        print(self.number_served)


restaurant = Restaurant("Cape Coast")
restaurant.restaurant_cuisine("Ghanaian")
restaurant.describe_restaurant()
restaurant.customers_served(23)
restaurant.more_customers(21)
