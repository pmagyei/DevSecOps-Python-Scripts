from pathlib import Path
import json
def get_stored_username(path):
    """Reads username if it exits"""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return f"{username}"
    else:
        return None

def get_new_username(path):
    """Prompt for username"""
    username = input("Name: ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """Greet user by name"""
    path = Path("./files/username.json")
    username = get_stored_username(path)
    if username:
        print(f"{username}")
    else:
        username = get_new_username(path)
        print(f"{username}")


greet_user()
