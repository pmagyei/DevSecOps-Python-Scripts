from pathlib import Path
import json

user_info = {}
path = Path("./files/user_info.json")
if path.exists():

    content = path.read_text()
    u_info = json.loads(content)
    print(u_info)



else:
    entries = int(input("How many entries:\n"))
    for _ in range(entries):
        name = input("Name: ")
        age = int(input("Age: "))
        city = input("City: ")
        user_info.update({name:[{"age":age}, {"city":city}]})
        content = json.dumps(user_info)
        path.write_text(content)
