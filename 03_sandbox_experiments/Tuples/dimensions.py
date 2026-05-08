dimensions = (200, 50) # tuple are defined by the prsence of a comma

# dimensions[0] = 250 TypeError: 'tuple' object does not support item assignment
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100) # a new value can be assigned to a variable to represent a tuple
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)