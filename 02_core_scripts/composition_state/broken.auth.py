class Authenticator:
    def __init__(self, password):
        self.password = password

    def get_token(self):
        return f"Token_{self.password}"

class Database:
    def __init__(self, db_name, password):
        self.db_name = db_name

        self.auth_module = Authenticator(password)

    def connect(self):

        token = self.auth_module.get_token()
        print(f"Connecting to {self.db_name} with {token}")


prod_db = Database("CustomerData", "super_secret_999")
prod_db.connect()

#prod_db.auth_module.password