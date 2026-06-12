#CDD
# __init__ will hold url
# __base__ to hold ip
# url and ip can be combined into a string using f"{url}/{ip}"
# try /except to use ConnectionError to catch failed connections, method should return {} to maintain consistency
import json
import requests
from pathlib import Path

class FilePath:
    def __init__(self):
        pass
    @staticmethod
    def path_to_file(file: str):
        output_path = Path(f"{file}")  # path to file
        return output_path

class ThreatIntelClient:
    def __init__(self):
        self.__base_url = "https://ipapi.co/"

    def scan_ip(self, target_ip: str) -> dict:
        target_url = f"{self.__base_url}{target_ip}/json/"
        try:
            response = requests.get(target_url)  # sends a get request to the target url
            api_response = response.json() # assigns response to variable
            return api_response

        except requests.exceptions.ConnectionError:
            print("error")
            return {}

class SaveFile:
    @staticmethod
    def save_to_file(api_resip):
        output_path = FilePath.path_to_file("google.json")
        with output_path.open("w", encoding="utf-8") as output_file:
            json.dump(api_resip, output_file, indent=4)  # json.dump serializes obj as a JSON format
            return output_file

path_file = FilePath.path_to_file("google.json")  #instantiate file path
call_api = ThreatIntelClient()
api_client_response = call_api.scan_ip("8.8.8.8")
save_file = SaveFile.save_to_file(api_client_response)


# sv = SaveFile.save_to_file("")
# call_api = ThreatIntelClient()  # instantiate object
# r_ip = call_api.scan_ip("8.8.8.8") # commands object to act
# print(r_ip)