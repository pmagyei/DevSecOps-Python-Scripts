from pathlib import Path
import json

username = input("Name:\n")

path = Path("./files/username.json")
contents = json.dumps(username)
path.write_text(contents)

print(f"{username} has been saved successfully")