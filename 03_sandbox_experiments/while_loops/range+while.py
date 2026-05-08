prompt = "\n What is your age:"
prompt += "\n type quit if done"


active = True
while active:
    user_age = input(prompt)

    if user_age.lower() == 'quit':
        active = False


    else:
        user_age = int(user_age)
        if user_age < 3:
            print("The ticket is free")
        elif 3 < user_age <= 12:
            print("print ticket is 10")
        elif user_age > 12:
            print("The the ticket is 15")



