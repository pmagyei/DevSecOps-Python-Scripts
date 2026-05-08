current_users = ['Lo', 'Mo', 'Joga', 'Ola', 'Pierre', 'Andrew']

new_users = ['ola', 'pierre', 'stona', 'conto']

for user in new_users:
    if user.title() in current_users:
        print(f"{user} has already been taken")
    else:
        print(f"{user} is available")