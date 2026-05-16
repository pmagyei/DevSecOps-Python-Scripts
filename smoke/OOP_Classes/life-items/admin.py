class User:
    def __init__(self, role,department):

        self.role = role
        self.department = department

class Admin(User):

    def __init__(self, role, department):
        super().__init__(role, department)
        # Make a Privileges instance as an attribute in the Admin class.
        self.privilege = Privilege(self.role)

    #privileges = ["can add post", "can delete post", "can ban user"]

   # def show_privileges(self):

    #    self.privileges
    #    print(f"{self.role} has the following privileges:")

    #    for privilege in self.privileges:
    #        print(privilege)

class Privilege:
    def __init__(self, role):
        self.privileges = ["can add post", "can delete post", "can ban user"]
        self.role = role

    def show_privileges(self):

        # Create a new instance of Admin and use your method to show its privileges.
        for privilege in self.privileges:
            print(f"{self.role} {privilege}")


admin_user = Admin('Admin', 'Infrastructure')

print(f"{admin_user.role} can have the following roles:")
admin_user.privilege.show_privileges()



