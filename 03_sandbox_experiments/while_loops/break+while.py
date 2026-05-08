
prompt = "Where do you want to travel?"
prompt += "\nType 'busy' if you do not want to travel"



active = True
location = input(prompt)
while active:
    if location != 'quit':
        print(location)

    else:
        if location == 'quit':
            print("exiting")
            break