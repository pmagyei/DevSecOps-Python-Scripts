# [] represent lists

bicycles =['trek', 'cannondale', 'redline', 'specialized']


#[x] x=number this will allows access to any element using the index

# print(bicycles[3].title()) # can be combined with string methods 

# positions start at 0 not 1

# print(bicycles[-1].lower())  #access last items in a list by using negative signs
#-1 last item from the list
# print(bicycles[-2].upper()) #-2 second last item from the list

# print(bicycles[3].title())

message = f"My first bike was a {bicycles[2].title()}"

print(message)