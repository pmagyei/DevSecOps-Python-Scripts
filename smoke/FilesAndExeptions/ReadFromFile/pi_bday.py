from pathlib import Path

path = Path("files/pi_million_digits.txt")
contents = path.read_text()

lines = contents.splitlines()

pi_string = ""

for line in lines:
    pi_string += line.strip()

birthday = input("enter your birthday")

if birthday in pi_string:
    print("your birthday is in pi")
else:
    print("your birthday does not appear")