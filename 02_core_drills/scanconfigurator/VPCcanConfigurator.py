# CDC

# FUNCTION: accept unknown number of IP addresses to scan and accept unknown number of ports
# INPUT: IP addresses and port numbers
# OUTPUT: Return a nested dictionary mapping each IP to the exact configuration

# Blueprint

# define function
def configure_scan(*ips, **configurations): # pass the arguments as parameters
    """Return a nested dictionary mapping each IP to Ports"""
    master_scan = {}
    for ip in ips:
        master_scan[ip] = configurations
            # use the data passed by the parameters to populate the dictionary

    return master_scan
    # return the dictionary to function call

vpc_scan = configure_scan("10.0.0.1", "192.168.1.50", timeout=30, stealth=True, port=443)

print(vpc_scan)# print the dictionary