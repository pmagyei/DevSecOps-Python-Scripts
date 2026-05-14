# CDD
# create a master list called active directory
# define parent class CloudUser
# Child class AdminUser must inherit from parent CloudUser


# write loop to loop through the nest dictionaries,
# extract the value
# if the role is standard: instantiate CloudUser
# if the role is Admin: instantiate AdminUser
# loop through the active directory list and print each user's name and their permissions

class CloudUser:
    """Defined Cloud User"""
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def get_permissions(self):
        """returns a list of users with read-only access"""
        standard_permission = ["read_only"]
        return standard_permission

class AdminUser(CloudUser):

    def __init__(self, name, department):

        super().__init__(self, name, department)
        def get_permissions(self):
            admin_permission = ["read_only", "write", "delete"]
            return admin_permission


new_hires = [
    {'name': 'Alice', 'department': 'Marketing', 'role': 'standard'},
    {'name': 'Bob', 'department': 'Engineering', 'role': 'admin'},
    {'name': 'Charlie', 'department': 'Sales', 'role': 'standard'}
]

for hire in new_hires:
    if (hire["role"]) == "standard":
       s_user = CloudUser(hire["role"], hire["department"])
       print(s_user.get_permissions())

    else:
        if (hire["role"]) == "admin":
            a_user = AdminUser(hire["role"], hire["department"])
            print(a_user.AdminUser.get_permissions())




