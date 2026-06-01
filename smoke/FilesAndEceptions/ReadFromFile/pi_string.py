from pathlib import Path

path = Path("files/pi_million_digits.txt")
contents = path.read_text()

lines = contents.splitlines()

pi_string = ""

for line in lines:
    pi_string += line.strip()



print(f"{pi_string[:52]}...")
# print(pi_string)
# print(len(pi_string))
