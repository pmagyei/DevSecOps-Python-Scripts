#CDD
# __init__ will hold url
# __base__ to hold ip
# url and ip can be combined into a string using f"{url}/{ip}"
# try/except to use ConnectionError to catch failed connections, method should return {} to maintain consistency

# use for loop to pass extracted ip addresses from log parser to threatintelclient
# append each response separately to file

import json
import requests
from pathlib import Path


class PathFile:
    # def __init__(self):
    #     pass
    @staticmethod
    def path_to_file(file: str) -> Path:
        output_path = Path(f"{file}")  # path to file
        return output_path

class ThreatIntelClient:
    def __init__(self):
        self.__base_url = "https://ipapi.co/"

    def scan_ip(self, target_ip: str) -> dict:
        target_url = f"{self.__base_url}{target_ip}/json/"
        try:
            response = requests.get(target_url)  # sends a get request to the target url
            # print(f"HTTP Status: {response.status_code}")
            # print(f"Raw Response: {response.text}")
            api_response = response.json() # assigns response to variable
            if api_response:
                print("API reply: saving response")
            return api_response

        except requests.exceptions.ConnectionError, requests.exceptions.JSONDecodeError:
            print("error")
            return {}

class SaveFile:
    @staticmethod
    def save_to_file(api_resp: dict, output_path) -> dict:
        # path_file = PathFile
        # output_path = path_file.path_to_file("")
        with output_path.open("a", encoding="utf-8") as output_file:
            json.dump(api_resp, output_file, indent=4)  # json.dump serializes obj as a JSON format
            return output_file

# path2_file = PathFile #instantiate file path
# p_file = path2_file.path_to_file("google.json")
# print(f"File:{p_file} has been saved")

# call_api = ThreatIntelClient()
# api_client_response = call_api.scan_ip("8.8.8.8")
# save_file = SaveFile.save_to_file(api_client_response, p_file)