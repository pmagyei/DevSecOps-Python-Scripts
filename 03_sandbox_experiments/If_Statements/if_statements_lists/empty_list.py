requested_toppings = []
#empty list evaluates to false
if requested_toppings:
    for requested_toppings in requested_toppings:
        print(f"Adding {requested_toppings}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")