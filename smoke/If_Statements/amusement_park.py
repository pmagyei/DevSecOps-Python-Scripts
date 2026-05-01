age = 65
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
# omit the else block for clearer logic within the code, each block must pass a specific test ot be executed
print(f"Your admission cost is {price}")