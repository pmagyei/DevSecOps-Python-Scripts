scan_results = [
    {'cve': 'CVE-2024-0001', 'base_score': 8.5, 'exploit_score': 3.2},
    {'cve': 'CVE-2024-0002', 'base_score': 5.0, 'exploit_score': 1.5},
    {'cve': 'CVE-2024-0003', 'base_score': 9.8, 'exploit_score': 3.9}
]

# the function only needs two values, carry out the calculation, and return the value.
def calculate_risk(base, exploit): # parameters pass data in the function body
    vulnerability_risk = (base * exploit / 2) # multiplies the passed parameters
    return vulnerability_risk # returns value to the function call

for result in scan_results: # iterates through each item in the list
        base_score = result['base_score'] # extracts value
        exploit_score = float(result['exploit_score']) # extracts value
        final_risk = calculate_risk(base_score, exploit_score) # calls the functions with assigned values to pass on to the function's parameters
        print(f"Vulnerability {result['cve']} has a total risk score of {round(final_risk, 2)}")
