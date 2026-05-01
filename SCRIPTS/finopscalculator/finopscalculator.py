active_instances = [
    {'instance_id': 'i-001abcd', 'type': 't2.micro', 'state': 'running'},
    {'instance_id': 'i-002efgh', 'type': 'm5.large', 'state': 'running'},
    {'instance_id': 'i-003ijkl', 'type': 't2.micro', 'state': 'stopped'},
    {'instance_id': 'i-004mnop', 'type': 'c5.xlarge', 'state': 'running'}
]

# Dictionary mapping server types to their hourly cost (in dollars)
hourly_pricing = {
    't2.micro': 0.02,
    'm5.large': 0.15,
    'c5.xlarge': 0.35
}

total_hourly_cost = 0.0

servers_running = []
for ins_info in active_instances:
    if ins_info['state'] == 'running':
        #print(ins_info['type'])
        server_type = ins_info['type']

        total_hourly_cost += hourly_pricing[server_type]
print(total_hourly_cost)








