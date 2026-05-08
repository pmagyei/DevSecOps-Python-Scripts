my_foods = ['pizza', 'falafel', 'carrot_cake']

friends_foods = my_foods[:]  #without [:] both variables point to the same list, changes to my food will appear on friends-food 


my_foods.append('cannoli')

friends_foods.append('ice cream')

print("My favourite foods are:")
print(my_foods)

print("\nMy freind's favourite foods are:")
print(friends_foods)