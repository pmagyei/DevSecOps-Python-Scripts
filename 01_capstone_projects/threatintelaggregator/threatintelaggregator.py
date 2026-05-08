# CDD
# FUNCTION: ingest an unknown number of feeds and returns a clean list
# INPUT: unknown number of feeds, list of nested dictionaries
# OUTPUT: combined list of single IP addresses with "high" severity, no duplicates

# comments == Blueprint
vendor_a = [{'ip': '10.0.0.5', 'sev': 'High'}, {'ip': '192.168.1.1', 'sev': 'Low'}]
vendor_b = [{'ip': '172.16.0.8', 'sev': 'High'}, {'ip': '10.0.0.5', 'sev': 'High'}]
vendor_c = [{'ip': '203.0.113.1', 'sev': 'Medium'}]


# define function with s positional argument
def aggregate_intel(*vendors: list) -> list:
    # include typehint to explicitly state what the function expects and returns
    ip_threats = []
    for vendor in vendors: # iterate through each vendor using a for loop
        for threat in vendor: # extract lists
             if threat['sev'] == "High": # extract IP from each list that has a "high" severity
                 ip_threats.append(threat['ip']) # appends IP to a new list if it has a high priority
    return list(set(ip_threats)) # returns list with no duplicates


v_ip = aggregate_intel(vendor_a, vendor_b, vendor_c)
print(v_ip)