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

StBu = StorageBucket("nna", "eu-west-2b") # instantiate the object
deploy_StBu = StBu.deploy() # command the object to act
print(deploy_StBu)

SeBu = SecureBucket("nna", "eu-west-2a", "placeholder")
deploy_SeBu = StBu.deploy()
print(deploy_SeBu)