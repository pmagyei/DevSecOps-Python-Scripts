banned_ips = []

system_running = True

print("=== Welcome to the Automated Firewall CLI ===")
print("Type 'quit' to exit the system.")
print("Type 'show' to view the current blocklist.\n")

while system_running:
    user_command = input("Enter an IP address to block(or a command)")
    if user_command == 'quit':
        system_running = False
        print("Shutting down firewall CLI...")
    elif user_command == 'show':
        print(banned_ips)
    else:
        banned_ips.append(user_command)
        print(f"{user_command} successfully blocked" )



