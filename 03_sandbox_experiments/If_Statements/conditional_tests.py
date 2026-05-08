# devices = ['pc', 'laptop', 'macbook', 'phone', 'monitor', 'webcam']
#
# device = 'headphones'
#
# for _ in devices:
#     if devices == _:
#         print(devices)
#     else:
#         print("no match")
#TRUE
#1
person1 = 23
person2 = 25
person3 = 27

print(person1 > person2 or person3 > person2)

#2
x = 671
b = 876
c = 998

print(c >= b and b > x)

#3

devices = ['pc', 'laptop', 'macbook', 'phone', 'monitor', 'webcam']

u_device = 'headphones'

print(u_device not in devices)

#4
car =  'Rolls Royce'

print(car.lower().strip() == 'rolls royce')


water = ['Spring', 'Mineral', 'Natural']

w = 'Spring'
if w in water:
    print(f"I can drink: {w} water")

#False


even_numbers = [121,35,46,57,65,6,7,8,90]

for _ in even_numbers:
    if _ % 2 == 0:
        print(f"Number {_} is an even number")

e_number = 44

print(e_number in even_numbers)

o_price = 24
sale_price = 15

print(o_price == sale_price)
print(o_price <= sale_price)


SUV1 = 'Blue'
SUV2 = 'Black'
SUV3 = 'Brown'

print(SUV3 != SUV2 and SUV1 == SUV3)
SUV3 = 'Blue'
SUV2 = 'Blue'
print(SUV3 != SUV2 or SUV1 != SUV3)