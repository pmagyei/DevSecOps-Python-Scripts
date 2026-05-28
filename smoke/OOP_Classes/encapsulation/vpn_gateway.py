class VPNGateway: #create the blueprint
    def __init__(self, gateway_ip, secret_key):

        self.gateway_ip = gateway_ip  # assign attributes to the object
        self.__secret = secret_key

    def get_status(self): # command the object to take action
        return f"VPN Gateway {self.gateway_ip} is active. Secret key is hidden."

    def update_status(self, old_key, new_key, admin_token): #pass parameters to the object
        if admin_token == "ad_tok":
            if old_key == self.__secret:
                self.__secret = new_key
                return "Key updated successfully" # returns string if old_key matches new key
            else:
                return "UNAUTHORIZED: Key update failed."
        else:
            return "Access denied"

    def view_secret(self, admin_token):
        if admin_token == "ad_tok":
            return self.__secret
        else:
            return "Access denied: insufficient privilege"

london_gw = VPNGateway("192.168.10.1", "secret")  # instantiate the object and assign it to a variable
print(london_gw.get_status()) # print the returned string

key_update = london_gw.update_status("secret", "new_secret", "ad_tok") # updates the secret key
print(key_update)

london_secret = london_gw.view_secret("ad_tok")
print(london_secret)

print("\n")

stockholm_gw = VPNGateway("192.168.10.2", "secret_2")
print(stockholm_gw.get_status())
key_update = stockholm_gw.update_status("secret", "new_secret", "token")
print(key_update)

london_secret = stockholm_gw.view_secret("token")
print(london_secret)

