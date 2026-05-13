class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof Woof"

dog = Dog("Guru")
#cat = Cat("Ivy")

print(f"{dog.name} says: {dog.speak()}")