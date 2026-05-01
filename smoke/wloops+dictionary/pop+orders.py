sandwich_orders = ['Chicken', 'Egg', 'Nutella']

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)


for sandwich in finished_sandwiches:
    print(f"The {sandwich} sandwich was made")
