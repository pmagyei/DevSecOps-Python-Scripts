class EvidenceLocker:
    """Build and incident tracker"""
    def __init__(self):
        self.logs = []

    def add_log(self, log_string):
        self.logs.append(log_string)

class SecurityIncident:
    """saves incident to incident locker"""

    def __init__(self, incident_id):

        self.incident_id = incident_id
        self.locker = EvidenceLocker()
    def show_incident_logs(self):

        print(f"{self.incident_id} has the following logs: ")
        for log in self.locker.logs:
            print(log)

sec_inc = SecurityIncident("INC-999")

sec_inc.locker.add_log("Unauthorized SSH attempts detected")
sec_inc.locker.add_log("Blocking IP address...")

print(sec_inc.locker.logs)
sec_inc.show_incident_logs()