start_loop = True
while start_loop:
    try:
        n1 = int(input("type number: "))
    except ValueError:
        print("Program accepts only integers")
    try:
        n2 = int(input("type number: "))
    except ValueError:
        print("Program accepts only integers")
    try:
        total = n1 + n2
    except NameError:
        print("Variable must be integers only")
    try:
        print(total)

    except NameError:
        print("Variable must be integers only")