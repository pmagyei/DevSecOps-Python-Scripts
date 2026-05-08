migration_inventory = {}

is_migrating = True

print("=== Asset Migration Tool Initialized ===")

while is_migrating:
    server_name = input("\nEnter server name: ")
    ip_address = input("\nenter ip address: ")
    migration_inventory[server_name] = ip_address
    print(f"Server {server_name} mapped to IP: {ip_address}")

    repeat = input("Would like to another server? (yes/no)").lower().strip()
    if repeat == 'no':
        is_migrating = False


for server, ip in migration_inventory.items():
    print(f"Server {server} mapped to IP: {ip}")
