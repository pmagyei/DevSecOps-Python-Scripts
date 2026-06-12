#CDD
# __init__ will hold url
# __base__ to hold ip
# url and ip can be combined into a string using f"{url}/{ip}"
# try /except to use ConnectionError to catch failed connections, method should return {} to maintain consistency
import json
import requests
from pathlib import Path

output_path = Path("google.json")
class ThreatIntelClient:
    def __init__(self):
        self.target_url = None
        self.__base_url = "https://ipapi.co/"

    def scan_ip(self, target_ip: str) -> dict:
        self.target_url = f"{self.__base_url}{target_ip}/json/"
        try:
            response = requests.get(self.target_url)
            api_response = response.json()
            with output_path.open("w", encoding="utf-8") as file:
                json.dump(api_response, file, indent=4) #json.dump serializes obj as a JSON format
            return api_response

        except requests.exceptions.ConnectionError:
            print("error")
            return {}

call_api = ThreatIntelClient()
r_ip = call_api.scan_ip("8.8.8.8")
print(r_ip)