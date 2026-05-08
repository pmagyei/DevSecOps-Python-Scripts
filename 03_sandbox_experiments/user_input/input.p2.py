prompt = "How many people are in the dinner group? "

user_input = int(input(prompt))

if user_input > 8:
    print("You will have to wait for a table")
else:
    print("A table is available now")

