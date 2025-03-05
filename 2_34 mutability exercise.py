
print("int")
number = 5
print("number:", number)
addr1 = id(number)
number += 2
print("number:", number)
addr2 = id(number)
print("addr1 == addr2:", addr1==addr2)
print( )

print("fruits")
#addr3
fruits = ["apple","banana","cherry"]
addr3 = id(fruits)
print("addr3:", addr3)
fruits += ["orange"]
addr4 = id(fruits)
print("addr4", addr4)
print("addr3 == addr4:", addr3 ==addr4)
