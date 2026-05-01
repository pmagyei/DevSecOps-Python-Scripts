
person_age = int(input(f"what is your age: \n"))

if person_age < 2:
    stage_of_life = 'baby'
    print(f"The person is a {stage_of_life}")
elif person_age <= 4:
    stage_of_life = 'toddler'
    print(f"The person is a {stage_of_life}")
elif person_age <= 12:
    stage_of_life = 'kid'
    print(f"The person is a {stage_of_life}")
elif person_age <= 19:
    stage_of_life = 'teenager'
    print(f"The person is a {stage_of_life}")
elif person_age >= 20:
    stage_of_life = 'adult'
    print(f"The person is a {stage_of_life}")
elif person_age <= 65:
    stage_of_life = 'elder'
    print(f"The person is a {stage_of_life}")