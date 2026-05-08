sandwich_orders = ['Chicken', 'Egg', 'Nutella', 'pastrami', 'pastrami', 'pastrami']

print('We have run out of pastrami')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)