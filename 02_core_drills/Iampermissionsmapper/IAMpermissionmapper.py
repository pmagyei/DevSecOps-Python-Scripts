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

for name, role in employees.items(): # .items() expands the list's key and values, these are assigned to name and role variables
    permission = role_permissions[role] # uses the value as a key to extract the value and assign it the variable
    if 'delete' in permission: # if the string 'delete' appears in the list which is assigned to the variable, the following block of code that is indented will be executed
        print(f"ALERT: {name} has highly privileged DELETE access")