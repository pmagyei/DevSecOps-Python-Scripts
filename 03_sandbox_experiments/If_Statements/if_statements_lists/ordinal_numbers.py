numbers = [1,2,3,4,5,6,7,8,9]

for _ in numbers:
    if _ < 2:
        print(f"{_}st")
    elif _ <= 2:
         print(f"{_}nd")
    elif _ <= 3:
         print(f"{_}rd")
    else:
        print(f"{_}th")