class Dog: # Class
    """Dog Model attempt"""
    # parameters
    def __init__(self, name, age):
        # self os required and must be first
        # a method is a function that's part of class
        """Initialize name and age attributes."""
        self.name = name # attribute: variables access through instances
        self.age = age

    def sit(self):
        # method
        """Simulate a dog sitting"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        # method
        """Simulate dog rolling over"""
        print(f"{self.name} rolled over!")

my_dog = Dog("Willie", 6)  # arguments, instance 1


# dot notation tells how python finds an attributes' value.
print(f"{my_dog.name} is {my_dog.age}")
my_dog.sit()

