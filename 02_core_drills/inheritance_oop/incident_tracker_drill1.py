class SecurityIncident:
    """creates an incident object to store and hold the evidence"""

    def __init__(self, incident_id, severity):

        self.incident_id = incident_id
        self.severity = severity
        self.evidence_logs = []

    def add_log(self, log_string):
        self.evidence_logs.append(log_string)
        return self.evidence_logs


    def triage(self):
        if self.severity == "High":
            return f"Escalating incident {self.incident_id} to Tier 2"
        else:
            return f"Escalating incident {self.incident_id} to Tier 1"



high_sec_event_log = SecurityIncident("SIID-1211", "High") # instantiate object
HsEl = high_sec_event_log.add_log("High Severity event detected")  # command object
high_sec_event_log.add_log("Malicious payload dropped") # command object
print(high_sec_event_log.triage())
print(HsEl)

low_sec_event_log = SecurityIncident("SIID-1212", "Low")

LsEl = low_sec_event_log.add_log("Low Severity event detected")
print(low_sec_event_log.triage())
print(LsEl)
