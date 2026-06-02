from pathlib import Path

path = Path("files/pi_digits.txt")
contents = path.read_text()
lines = contents.splitlines() # returns list of all lines in the file

for line in lines:
    print(line)