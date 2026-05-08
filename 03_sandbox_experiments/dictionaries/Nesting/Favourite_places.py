favourite_place = {
    'Mqrgot': ['London', 'Manchester', 'Birmingham'],
    'Dante': ['Manchester', 'Palmanova', 'Stockholm'],
    'Ehmyr': ['Accra', 'Tokyo', 'Jburg']
}


for person, locations in favourite_place.items():
    print(f"{person}'s favourite places are:")

    for location in locations:
        print(f"{location}")
    print("\n")

