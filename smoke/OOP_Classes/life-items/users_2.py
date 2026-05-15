class User:
    """"""
    def __init__(self, first_name, last_name, age, ethnicity, birthplace):
        """Initialize attributes to describe user"""
        self.f_name = first_name
        self.l_name = last_name
        self.age = age
        self.ethnicity = ethnicity
        self.birthplace = birthplace
        self.login_attempt = 0

    def describe_user(self): #method
        """Prints summary of user"""
        print("\n")
        print(f"Displaying {self.f_name} {self.l_name}'s profile summary:")
        print(self.age)
        print(self.ethnicity)
        print(self.birthplace)

    def increment_login_attempts(self, attempts):
        """Increments login at each attempt"""
        if attempts >= self.login_attempt:
            self.login_attempt = attempts
            self.login_attempt += 1
            print(f"{self.login_attempt} login attempts have been made")
        else:
            print("Login attempts rollback now allowed")

    def reset_login_attempts(self):
        """resets login attempts"""
        self.login_attempt = 0
        print(self.login_attempt)

    def greet_user(self): #method
        """Print personalized greeting"""
        print(f"Hi {self.f_name} welcome to the World of Automation")

user_1 = User("Prince", "Agyei", 26, "Ghanaian", "Udine")
# user_1.describe_user()
# user_1.greet_user()
user_1.increment_login_attempts(1)
user_1.reset_login_attempts()

# user_2 = User("Angel", "Sun", 29, "Brazilian", "Brasília")
# user_2.describe_user()
# user_2.greet_user()
#
# user_3 = User("Christopher", "Tron", 32, "Swedish", "Stockholm")
# user_3.describe_user()
# user_3.greet_user()



