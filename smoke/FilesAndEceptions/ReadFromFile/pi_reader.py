from pathlib import Path

path = Path("files/pi_digits.txt")

contents = path.read_text().rstrip()
print(contents)
# contents = contents.rstrip()
# print(contents)

