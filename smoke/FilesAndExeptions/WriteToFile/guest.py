from pathlib import Path

name = input("What is your name: \n")

path = Path("../files/guest.txt")

path.write_text(name)
