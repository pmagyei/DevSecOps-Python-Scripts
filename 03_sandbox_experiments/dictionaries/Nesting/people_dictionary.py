Dante = {'first_name': 'Dante', 'last_name': 'Jit', 'age': 26, 'city': 'Leeds'}

Priscilla = {'first_name': 'Priscilla', 'last_name': 'Agyei', 'age': 26, 'city': 'Udine'}

Edna = {'first_name': 'Edna', 'last_name': 'Ofo', 'age': 26, 'city': 'Manchester'}

people = [Dante, Priscilla, Edna]

for person in people:
    print(f"First name: {person['first_name']}")
    print(f"Last name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"Location: {person['city']}")
    print("\n")

# for person in people:
#     for key, value in person.items():
#         print(key)
#         print(value)
#         print("\n")