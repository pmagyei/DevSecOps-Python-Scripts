usernames = []
# usernames = ['sarah', 'alpha', 'lisa', 'Anna', 'Pietro', 'Admin']

if usernames:
    for user in usernames:
        if user.lower() == 'admin':
            print(f"Hi {user.lower()}, what would like to do today?")
        else:
            print(f"Welcome back {user.lower()}")
else:
    print("We need more users")
