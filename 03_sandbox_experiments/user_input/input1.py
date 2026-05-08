prompt = "Share your name for personalisation"  # assigns 1st part of message t variable

prompt += "\nWhat is your first name? "  #+= assigns 2nd line + previous value

#print(prompt)
name = input(prompt)

print(f"\nHello, {name}")


#input() python interprets everything the user enters as a string
