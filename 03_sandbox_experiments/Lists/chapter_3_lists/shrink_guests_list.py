colours = ['Purple', 'Yellow', 'Blue', 'Red', 'Brown', 'Black', 'Green', 'Rose', 'Pink']

print("I can only invite two colours for dinner")

p=colours.pop(-1)
print(f"I'm sorry {p} I can no longer invite you")
#pop deletes value and makes it reusable
p=colours.pop(-1)
print(f"I'm sorry {p} I can no longer invite you")
p=colours.pop(-1)
print(f"I'm sorry {p} I can no longer invite you")
p=colours.pop(-1)
print(f"I'm sorry {p} I can no longer invite you")
p=colours.pop(-1)
print(f"I'm sorry {p} I can no longer invite you")
p=colours.pop(-1)
print(f"I'm sorry {p} I can no longer invite you")
p=colours.pop(-1)
print(f"I'm sorry {p} I can no longer invite you")

print(f"Hi {colours[0]}, Hi {colours[1]} you are still invited")

del colours[0]
del colours[0]
print(colours)