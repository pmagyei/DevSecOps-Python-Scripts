class APIConnector:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def connect(self):
        print(f"Connecting to {self.endpoint}...")

class FirewallAPI(APIConnector):
    def __init__(self, endpoint, api_key):
        super().__init__(endpoint)
        self.api_key = api_key

    def authenticate(self):
        print(f"Authenticating to firewall using key: {self.api_key}")


# Execution Phase
fw_connection = FirewallAPI("https://10.0.0.1/api", "super_secret_key_999")
FirewallAPI.connect(fw_connection)
fw_connection.authenticate()