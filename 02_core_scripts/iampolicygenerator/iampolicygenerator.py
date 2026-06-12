# CDC
# the script will have a function return a nested dictionary
# the function call should pass a list and multiple keyword arguments as arguments
# the function should return a dictionary as a value with nested list and dictionaries

# master_policy = {} global variable, use variables inside code blocks to avoid overwriting
def generate_policy(role, allowed_actions, **iam_policy):
    """generates an IAM policy"""
    #master_policy = {'Role_name': role, 'Permission': allowed_actions, 'Metadata Tags': iam_policy}

    master_policy = {} #creates a new dictionary

    master_policy['Role_name'] = role # assigns key to DevTeam
    master_policy['Permission'] = allowed_actions # assigns key to the s3 bucket permissions
    master_policy['Metadata Tags'] = iam_policy # assigns key to iam_policy value
    return master_policy

policy = generate_policy("DevTeam", ["s3:GetObject", "s3:PutObject"],
                Department="Engineering", Environment="Prod")

print(policy)