available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']


for topping in requested_toppings:
    if topping in available_toppings:
        print(f"Adding {topping}")
    else:
        print(f"We don't have {topping}")

print("\nFinished making your pizza")