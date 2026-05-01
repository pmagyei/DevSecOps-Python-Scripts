players = ['charles', 'martina', 'micheal', 'florence', 'eli']
#print(players[0:5:2]) slicing allows output of specific elements in a list


print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())