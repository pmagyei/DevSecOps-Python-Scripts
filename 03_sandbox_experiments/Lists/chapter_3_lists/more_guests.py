colours = ['Yellow', 'Blue', 'Red', 'Black', 'Green', 'Rose']
colours.insert(0,'Purple')
colours.insert(4,'Brown')
colours.append('Pink')


print("A bigger tables has been found, Purple, Brown and Pink will be joining us.")

def invitation():
    for colour in colours:
        print(f"Hi {colour.title()} The dinner is this Friday, see you soon ;) ")

invitation()

print(colours)