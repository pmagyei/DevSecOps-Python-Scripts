from abc import ABC, abstractmethod
# Create two classes: WebFrontend and DataBaseBackend
# define the constructor to initialize the object state
# assign attributes and self to reference the current state
# add lockdown method in both classes to bind the function respective in each class
# create a list and add each class within the list
# use a for loop to trigger each class and use .notation to comamnd the object
# return the string of the action taken

class NetworkNode(ABC):
    @abstractmethod
    def lockdown(self):
        pass

class WebFrontend(NetworkNode):
    # constructor
    def __init__(self, ip_address):
        self.ip = ip_address # attribute stored on object

    def lockdown(self) -> str: # function bound to object
        return f"{self.ip} isolated from network" # returns string


class DataBaseBackend(NetworkNode):

    def __init__(self, database_name):
        self.db_name = database_name

    def lockdown(self) -> str:
        return f"{self.db_name}, encrypting storage at rest....."

class CloudStorage(NetworkNode):
    def __init__(self, bucket_name):

        self.bucket = bucket_name

    def secure_bucket(self):
        return f"{self.bucket}"

    # def lockdown(self) -> str:
    #     return ""


# build and assign to a variable
my_server = WebFrontend("192.168.0.1")
my_db = DataBaseBackend("RDS-01")
my_cloud = CloudStorage("my_bucket1") # cannot instantiate due to abstraction, class must have lockdown method

# use the variables in the list
Backends = [my_server, my_db, my_cloud] # instantiates objects in the list.
# list is used to iterate each class and trigger methods

for backend in Backends: # for loop
    print(backend.lockdown()) #  instances are commanded to use the method using . notation
