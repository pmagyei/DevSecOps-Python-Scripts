class StorageBucket:

    def __init__(self, bucket_name, region):
        """parent blueprint"""

        self.bucket_name = bucket_name
        self.region = region

    def deploy(self):
        return f"Deploying standard bucket: {self.bucket_name} in {self.region}"

class SecureBucket(StorageBucket):

    def __init__(self, bucket_name, region, kms_key):
        super().__init__(bucket_name, region)

        self.kms_key = kms_key

    def deploy(self):

        return f"Deploying secure bucket: {self.bucket_name} with key {self.kms_key}"


# final result of the entire chain returns string
SeBu = SecureBucket("logging_bucket", "eu-west-2a", "placeholder").deploy() #builds object, it has properties, memory and state, object immediately runs the method
print(SeBu) # method returns a string
# object has no variable holding on to it, object is deleted from RAM


Sec_Buck = SecureBucket("files_bucket", "eu-west-2b", "placeholder") # instantiates object and assigns object to variable, SB holds the object
print(Sec_Buck) # prints object (saved in RAM)
deployment_status = Sec_Buck.deploy() # deployment status holds the string
print(deployment_status)