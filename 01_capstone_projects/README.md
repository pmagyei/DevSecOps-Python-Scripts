DevSecOps Python Toolkit

A collection of automated Python scripts designed to solve common Cloud Security and DevSecOps challenges.

Tools Included:

1. [threatlistcombiner](./threatlistcombiner)
What it does: Combines to sets of IP addresses and removes any duplicates
The Engineering: Used both mutating (by extending the lissy) and non-mutating (by adding lists together and assigning them to a new value) code to combine the lists.

2. [cvss_riskcalculator](./cvss_riskcalculator)
What it does: Extracts base_error and exploit_score and outputs a final risk value
The Engineering: Iterates through each item in the list, extracts values, performa calculation and returns the final score.
3. [VPCscanconfigurator](./scanconfigurator)
What it does: accepts an unknown number of IP addresses and ports it then returns a nested dictionary mapping each IP to the exact configuration
The Engineering: passes positional and keywords arguments as parameters. a for loop is used to extract each ip to the configuration.
4. [threatintelaggregator](./threatintelaggregator)
What it does: ingest an unknown number of feeds and returns a clean list
The Engineering: include typehint to explicitly state what the function expects and returns, uses 2 for loops to iterate through each vendor and dictionary within each vendor
extract IP from each list that has a "high" severity, appends IP to a new list if it has a high priority, returns lists with no duplicates