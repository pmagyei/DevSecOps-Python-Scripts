def make_pizza(size, *toppings):
    """Print the list of toppings that have beem requested."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'Margherita')
make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')