fav_num = {
    'Anna': [91, 34, 67, 67],
    'Matteo': [4, 63, 82, 777, 12],
    'Lulu': [35, 75, 300, 54],
    'Michele': [65, 32, 53, 21],
}


for name, numbers in fav_num.items():
    print(f"{name}'s favorite number are: ")

    for number in numbers:
        print(number)

print(f"Anna's favorite number is: {fav_num['Anna']}")
print(f"Matteo's favorite number is: {fav_num['Matteo']}")
print(f"Lulu's favorite number is: {fav_num['Lulu']}")
print(f"Michele's favorite number is: {fav_num['Michele']}")