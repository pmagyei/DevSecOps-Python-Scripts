server_inventory = {
    "server-01": {"os": "Ubuntu_18", "ip": "10.0.0.1"},
    "server-02": {"os": "Windows_2012", "ip": "10.0.0.2"}
}

os_threat_levels = {
    'Ubuntu_18': 'Critical',
    'Ubuntu_22': 'Safe',
    'CentOS_7': 'High',
    'Windows_2012': 'Critical'
}
for server, details in server_inventory.items():  # details is a value to server_inventory. details is a dictionary
    # details.get() on it to find the 'os'(key)
    current_os = details.get("os", "Unknown")  #current os = Ubuntu_18/Windows_2012 #if OS key doesn't exist its replaced with unknown

    # OS is used to get the threat level from os_threat_levels dictionary
    threat = os_threat_levels.get(current_os, "No Data")
    print(f"{server}: {threat}")
