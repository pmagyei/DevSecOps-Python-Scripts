from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"Circle with radius {self.radius}"
    
    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f"Square with side {self.side}"

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def __str__(self):
        return f"Triangle with base {self.base} and height {self.height}"

    def area(self):
        return self.base * self.height * 0.5

shapes = [Circle(4), Square(5), Triangle(6, 7)]

for shape in shapes:
    print(f"{shape.area()}cm")
