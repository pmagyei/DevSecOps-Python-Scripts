# Dictionary 1: Employee job titles
employees = {
    'alice_smith': 'developer',
    'bob_jones': 'admin',
    'charlie_doe': 'intern',
    'diana_prince': 'developer'
}

# Dictionary 2: The permissions granted to each job title
role_permissions = {
    'admin': ['read', 'write', 'delete', 'create_users'],
    'developer': ['read', 'write'],
    'intern': ['read']
}

for name, role in employees.items():
    permission = role_permissions[role]
    if 'delete' in permission:
        print(f"ALERT: {name} has highly privileged DELETE access")