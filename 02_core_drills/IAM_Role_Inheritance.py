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
    def __init__(self, v_name, v_department): # init method defines main attributes of parent class
        # __init__ is the constructor, object is born here                      # attributes
        self.name = v_name # attaches variable of the parameter to the object's memory (self)
        self.department = v_department
        self.active_directory = []

    def get_permissions(self): # calling this method executes the indented block
        # self allows access to anything in the objects memory
        # method is function attached to an object
        """returns a list of users with read-only access"""
        self.active_directory = ["read_only"]  #calls the attribute and appends an element, mutates the list
        for perm in self.active_directory: # iterates through the list of permissions in the active directory
            print(f"{self.name} has {perm} permissions") # f string to print name and permission associated to user
        # return active_directory

class AdminUser(CloudUser): # tells python CloudUser is the parent, establishes inheritance
    # copies every single line of code from ClouUser(parent) class into AdminUser (child) class

    def __init__(self, name, department):
        super().__init__(name, department) # super passes parent's __init__ to allow attributes accessible to the child

    def get_permissions(self): #overrides parent's method
        # method overriding, parent already has get_permissions
        # defining the same method in the child class tells python to ignore the parent's class
        # can be used to give Admins elevated privileges
        self.active_directory = ["read_only", "write", "delete"]
        for perm in self.active_directory:
            print(f"{self.name} has {perm} permissions")

new_hires = [
    {'name': 'Alice', 'department': 'Marketing', 'role': 'standard'},
    {'name': 'Bob', 'department': 'Engineering', 'role': 'admin'},
    {'name': 'Charlie', 'department': 'Sales', 'role': 'standard'}
]

active_directory = []

for hire in new_hires: # for loop to iterate each dictionary
# objects are built here
    if (hire["role"]) in "standard":  # if the string standard appears in the key, execute the indented block
       s_user = CloudUser(hire["name"], hire["department"])  # instantiate CloudUser and assign the object to s_user
       # s_user.get_permissions() # s_user returns assigned permission by calling the .getpermission()
       active_directory.append(s_user)

    else:
        if (hire["role"]) == "admin":
            a_user = AdminUser(hire["name"], hire["department"])
            # a_user.get_permissions()
            active_directory.append(a_user)

for user in active_directory:
    user.get_permissions()