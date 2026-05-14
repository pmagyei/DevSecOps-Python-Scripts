DevSecOps Python Toolkit

A collection of automated Python scripts designed to solve common Cloud Security and DevSecOps challenges.

Tools Included:

1. Port Scanner (SCRIPTS/portscanner)
What it does: An interactive CLI tool that prompts engineers for target ports.
The Engineering: Implements try/except error handling to prevent application crashes from bad user input during live security audits.

2. (SCRIPTS/rawlogparser)
What it does: Ingests logs and isolates IPs triggering 404 errors.
The Engineering: Utilizes dynamic string splitting to extract data without relying on hardcoded indexes.

3. (SCRIPTS/patchmanagement)
What it does: Looks up at the Operating System of each server, checks the threat level of the OS, if its 'critical' or 'high', adds that sever to the vulnerable servers list.
The Engineering: Leverages the value of a dictionary as a key in another dictionary to extract the value.

4. (SCRIPTS/Iampermissionmapper)
What it does: Check each employee's role and the assigned permission, employees with the 'delete permission' are printed
The Engineering: bridges the two datasets, extracts the value of a dictionary by using the value of another dictionary as the key

5. (SCRIPTS/finopscalculator)
What it does: Calculates how much the total running compute is costing each hour
The Engineering: Extracts the server type by using a key, uses the type to look up the price and adds it the total




