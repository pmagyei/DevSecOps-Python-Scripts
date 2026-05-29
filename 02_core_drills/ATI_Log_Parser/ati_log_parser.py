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

class FileReader:
    def __init__(self, log_file="audit_logs.txt"): # default file name, if file name or path changes, can be edited
        # when instantiating
        self.audit_log_file = log_file # file name/path set as attribute

    def __iter__(self):

    def analyze(self):
        try: # try/except if file is found reads prints it out
            with open(self.audit_log_file, "r") as file:
                return file.read()

        except FileNotFoundError: # fails gracefully if file is not found
            print("File not found")



class RootLogAnalyser(ABC):

    @abstractmethod
    def analyze(self): # enforces all child classes to have this method
        pass

class CloudtrailAnalyzer(RootLogAnalyser):

    def __init__(self):
        self.file_handler = FileReader()
        self.__threat_list = []

    def analyze(self):
        data = self.file_handler

        for line in data:
            if line in "UNAUTHORIZED":
                self.__threat_list.append(line)
    def get_report(self):
        return f"{self.__threat_list}"














#2nd sprint
class VPCFlowAnalyzer(RootLogAnalyser):

    def analyze(self):
        pass


