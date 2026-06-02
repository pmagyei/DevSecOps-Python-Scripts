from pathlib import Path

path = Path("../files/programming.txt")

contents = "I am an Engineer\n"
contents += "I am a Programmer\n"
contents += "I can automate\n"

path.write_text(contents)