class Restaurant:
    """Prints and describes"""

    def __init__(self, restaurant_name, cuisine_type):
        """initialize attributes to dscribe restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """describe cuisine type"""
        print(f"{self.restaurant_name} is a nice restaurant")
        print(f"{self.cuisine_type} cuisine is nice\n")

    def open_restaurant(self):
        """describe's restaurant openings"""
        print(f"{self.restaurant_name} is open everyday until Midnight")

restaurant = Restaurant("PIPI's", "Italian")
restaurant_1 = Restaurant("Cape Coast", "Ghanaian")
restaurant_2 = Restaurant("Nando's", "South African")

restaurant.describe_restaurant()
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()