cloud_user = {
    'username': 'jdoe_admin',
    'department': 'security',
    'resources': {
        'database_1': 45.50,
        'storage_bucket': 12.00,
        'web_server': 85.00
    }
}

(cloud_user['status']) = 'active'

total_bill = 0

for key, bill in cloud_user['resources'].items():
    total_bill += bill
print(f"User{cloud_user['username']} in the {cloud_user['department']} department has total monthly bill of ${total_bill}. The account is {cloud_user['status']}.")