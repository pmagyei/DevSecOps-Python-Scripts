rivers = {'nile': 'africa', 'amazon': 'south america', 'yangtze': 'china'}

for river, location in rivers.items():
    print(f"The {river.title()} river is found in {location.title()}.\n")

for river in rivers.keys():
    print(river.title())

print("\n")

for location in rivers.values():
    print(location.title())