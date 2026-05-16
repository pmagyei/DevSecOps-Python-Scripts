class User:
    def __init__(self, role,department):

        self.role = role
        self.department = department

class Admin(User):

    def __init__(self, role, department): # constructor hands the parameters to super()
        super().__init__(role, department) # Admin class pass the data to the Parent class
        # Make a Privileges instance as an attribute in the Admin class.

        self.privilege = Privilege(self.role) # nested component object
        # passing the privileges and role as an argument to pass data between classes
        # composition
class Privilege:
    def __init__(self, role): #role passed from Admin
        self.privileges = ["can add post", "can delete post", "can ban user"]
        self.role = role # attribute defined by role passed from admin

    def show_privileges(self):
        # Create a new instance of Admin and use your method to show its privileges.
        for privilege in self.privileges:
            print(f"{self.role} {privilege}")


admin_user = Admin('Admin', 'Infrastructure') # calls admin class to build object/instance

print(f"{admin_user.role} can have the following roles:")
admin_user.privilege.show_privileges()

print(admin_user.privilege.privileges)