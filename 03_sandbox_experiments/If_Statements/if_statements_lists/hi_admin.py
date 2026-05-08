usernames = ['sarah', 'alpha', 'lisa', 'Anna', 'Pietro', 'Admin']

for user in usernames:
    if user.lower() == 'admin':
        print(f"Hi {user.lower()}, what would like to do today?")
    else:
        print(f"Welcome back {user.lower()}")
