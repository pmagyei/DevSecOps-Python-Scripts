class NetworkInterface:
    def __init__(self, ip_address, subnet):
        """network interface component handling the network state"""
        self.ip_address = ip_address
        self.subnet = subnet

class EC2instance:
    def __init__(self, hostname, ip_address, subnet):
        """Object that delegates networking to an ENI component """
        self.eni = NetworkInterface(ip_address, subnet)
        self.hostname = hostname

    def get_network(self):
        
        print(f"The host name of this server is {self.hostname}")
        print(f"This server has the IP: {self.eni.ip_address} and belongs to the subnet: {self.eni.subnet}")

ec2 = EC2instance("Server01", "172.18.10.1", "172.18.10.0/28" ) # instantiate the object

ec2.get_network() # command the object
