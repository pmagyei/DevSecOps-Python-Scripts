colours = ['Yellow', 'Blue', 'Red', 'Black', 'Green', 'White']
print(f"{colours[5]} cannot make it to dinner :(, Rose is coming instead")
colours[5] = 'Rose'

#print(colours)

def invitation():
    for colour in colours:
        print(f"Hi {colour.title()} The dinner is this Friday, see you soon ;) ")

invitation()
print(colours)