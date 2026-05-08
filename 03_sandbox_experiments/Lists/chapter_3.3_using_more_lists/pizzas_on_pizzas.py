my_foods = ['pizza', 'falafel', 'carrot_cake']

friends_foods = my_foods[:]


my_foods.append('pasta')
friends_foods.append('fried_rice')

print("My favourite foods are:")
for food in my_foods:
    print(food)
print("\n")
print("My friend's favourite foods are:")
for cibo in friends_foods:
    print(cibo)