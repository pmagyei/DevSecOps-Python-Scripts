class User:
    def __init__(self, role,department):

        self.role = role
        self.department = department

class Admin(User):

    def __init__(self, role, department):
        super().__init__(role, department)

    privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):

        self.privileges
        print(f"{self.role} has the following privileges:")

        for privilege in self.privileges:
            print(privilege)


admin_user = Admin('Admin', 'Infrastructure')

admin_user.show_privileges()


