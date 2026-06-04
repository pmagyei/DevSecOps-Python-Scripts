from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
loop = True
while loop:
    first = input("\nPlease give  me a first name: ")
    if first == "q":
        break
    last = input("\nPlease give me your last name:")
    if last == "q":
        break

    formatted_name = get_formatted_name(first, last)
    print(f"Your name is: {formatted_name}.")