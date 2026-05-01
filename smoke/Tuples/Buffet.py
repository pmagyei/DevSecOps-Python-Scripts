buffet_cuisine = ('Italian', 'Soul_Food', 'African', 'Indian', 'Asinan', 'Oriental')


# buffet_cuisine[0] = 'AM' TypeError: 'tuple' object does not support item assignment

for cuisine in buffet_cuisine:
    print(cuisine)

print('\n')
buffet_cuisine = ('Italian', 'Soul_Food', 'African', 'Indian', 'Carribean', 'Mediterranean')
for cuisine in buffet_cuisine:
    print(cuisine)