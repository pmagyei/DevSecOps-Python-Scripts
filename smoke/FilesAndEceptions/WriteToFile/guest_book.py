from pathlib import Path

start_loop = True
guest_list = ""

path = Path("../files/guest_book.txt")
while start_loop:
    name = input("Type Name you want in the guest book or Exit to quit. \n")
    if name != "quit":
        guest_list += f"{name}\n"
    else:
        start_loop = False
        print("The program ended")

path.write_text(guest_list)
