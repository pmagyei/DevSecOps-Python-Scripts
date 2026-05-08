
prompt = "\nEnter a topping for you Pizza:"
prompt += "\ntype 'quit' when you are done\n"


# active = True
# while active:
#     topping = input(prompt)
#     if topping == 'quit':
#         active = False
#         print("The program ended")
#         break

prompt = "\nEnter a topping for you Pizza:"
prompt += "\ntype 'quit' when you are done\n"
topping = ""
while topping != 'quit':
    topping = input(prompt)
    if topping == 'quit':
        print("no more selections")
        break
    else:
        print(f"{topping.title()} will be added to your Pizza")