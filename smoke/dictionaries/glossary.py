programming_words = {'Variable': 'Represent a value that is pointed at',
                     'Tuples': ' Immutable values',
                     'lists': 'used to store multiple values that can be accessed by index',
                     'dictionaries': 'stores data as key value pairs, values can be access by the key',
                     'list_comprehensions': 'generates a list in line of code by using the for loop and new elements in one line',
                     'slicing': 'used to define specific values in a list or copy a whole list',
                     'integer': 'is a whole number',
                     'float': 'is a decimal number',
                     'indentation': 'defines how Python will run the code',
                     'Boolean': 'Has the value of either: True or False',
                     'PEP 8': 'Best practices Style guideline for Python',
                     }
#
# print(f"Definition of a Variable : {programming_words['Variable']}\n")
# print(f"Definition of a Tuples : {programming_words['Tuples']}\n")
# print(f"Definition of a lists : {programming_words['lists']}\n")
# print(f"Definition of a dictionaries : {programming_words['dictionaries']}\n")
# print(f"Definition of a Variable : {programming_words['Variable']}\n")
# print(f"Definition of a list_comprehensions : {programming_words['list_comprehensions']}\n")
# print(f"Definition of a slicing : {programming_words['slicing']}\n")


for word, definition in programming_words.items():
    print(f"A {word.title()} {definition}" )