class Person:
    def __init__(self, name, age):
        self.__name = name

        @property
        def name(self):
            return self.__name
        @name.setter
        def name(self, name):
            self.__name = name

person = Person("John", 25)
print(person.name)
person.name = "Jane"

print(person.name)