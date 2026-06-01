from pathlib import Path


path = Path("files/learning_python.txt")#

contents = path.read_text()

lines = contents.splitlines()
#print(lines)
learn_lines = ""

for line in lines:
    learn_lines += line

print(learn_lines)
# print("\n")
# print(contents.replace("Python", "Bash"))

