class Restaurant:

    def __init__(self, restaurant_name):

        self.restaurant = restaurant_name

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name):
        super().__init__(restaurant_name)

        self.flavours = []

    def get_flavours(self, flavour):

        self.flavours = [flavour]
        # self.flavours.append(flavour)
        for flavour in self.flavours:
            print(f"The {self.restaurant} sells {flavour} flavoured icecream")


restaurant = IceCreamStand("IceCreamStand")

restaurant.get_flavours("Vanilla")

