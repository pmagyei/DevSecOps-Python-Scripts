pet1 = {'kind': 'Dog', 'owner': 'Alfie'}
pet2 = {'kind': 'Cat', 'owner': 'Amanda'}
pet3 = {'kind': 'Elephant', 'owner': 'Dante'}
pet4 = {'kind': 'Rabbit', 'owner': 'Bunnie'}
pet5 = {'kind': 'Panda', 'owner': 'Ehmyr'}


pets = [pet1, pet2, pet3, pet4, pet5]

for pet in pets:
    print(pet['kind'])
    print(pet['owner'])