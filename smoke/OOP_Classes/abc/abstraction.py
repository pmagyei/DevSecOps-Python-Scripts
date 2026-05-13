from abc import ABC, abstractmethod


class Vehicle(ABC):
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Car is moving")

class Boat(Vehicle):
    def move(self):
        print("Boat is moving")#

car = Car()
car.move()

boat = Boat()
boat.move()