motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']


# last_owned= motorcycles.pop(0).title() #you can remove an item from any position by indexing the number in the pop(#)

#print(f"The last motorcyle I owned was a {last_owned}")

# use del to delete item from list and not use it again

# use pop() to use an item and use at the same time
# after pop is used item is no longer in the list

print(motorcycles)

#motorcycles.remove('ducati') # remove if position of the value is unknown
#print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")