#numbers = list(range(1, 11))

# for number in numbers:
#     print(number ** 3)


cube_comprehension = [number ** 3 for number in range(1, 11)]

print(cube_comprehension)