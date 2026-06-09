# CDD
# ABC interface: RootLogAnalyzer
# abstract method: .analyze
# file reader class
# child classes:
# CloudTrailAnalyzer
# VPCFlowAnalyzer
# child classes to have the abstract method: loganalyzer()
# list of malicious IPs or events discovered during the scan must be locked down: self.__ip_threat_list =[]
# unknown concept: with opan() as
# Crash prevention: try and except FileNotFoundError
#component: self.file_handler = FileReader()

from abc import ABC, abstractmethod # import abstract method to enforce child classes to have a method
import re

class FileReader:
    def __init__(self, log_file): # default file name, if file name or path changes, can be edited
        # when instantiating
        self.audit_log_file = log_file # file name/path set as attribute

    def analyze_file(self) -> list[str]: # function returns a list containing only strings
        try: # try/except if file is found reads prints it out
            with open(self.audit_log_file, "r") as file:
                return file.readlines()

        except FileNotFoundError: # fails gracefully if file is not found
            print("File not found")  # this will cause a
            return []

class RootLogAnalyser(ABC):

    @abstractmethod
    def analyze(self): # enforces all child classes to have this method
        pass

class CloudtrailAnalyzer(RootLogAnalyser):

    def __init__(self, log_file):
        self.file_handler = FileReader(log_file)
        # __ encapsulation to prevent fake IP injections
        self.__threat_list = []
        self.__threat_ip = []

    def analyze(self):

        ip_pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
        audit_file = self.file_handler.analyze_file() # file with a list of strings is returned
        for line in audit_file: # iterates over each line in the file
            if "UNAUTHORIZED" in line: # if UNAUTHORIZED is in the file, it appends it to the list
                clean_line = line.strip() # removes the \n
                self.__threat_list.append(clean_line)

                extracted_ips =  re.findall(ip_pattern, clean_line) # regex to extract ip addresses
                for lines in extracted_ips:
                    self.__threat_ip.append(lines)

    def get_report(self) -> str:
        return f"{self.__threat_list}" # returns list containing unauthorized attempts

    def block_threats(self):

        ip_addresses = self.__threat_ip
        for ip in ip_addresses:
            print(f"Executing firewall drop rule for {ip}:")

audit_log_file = CloudtrailAnalyzer("audit_logs.txt")
audit_log_file.analyze()

report = audit_log_file.get_report()
#print(report)

audit_log_file.block_threats()

#2nd sprint
class VPCFlowAnalyzer(RootLogAnalyser):

    def analyze(self):
        pass