dream_vacation = {}

dream_active = True

while dream_active:
    name = input("\nWhat is your name")
    destination = input("\nWhat is your dream vacation")

    dream_vacation[name] = destination
    repeat = input('Would you like to another user? (yes / no)')
    if repeat == 'no':
        dream_active = False


print('----poll results----')
for name, vacation in dream_vacation.items():
    print(f"{name} dream vacation is {vacation}")