
numbers = [0,1,2,3,4,5,6,7,8]
print(type(numbers))

#task1

if 7 in numbers:
    print("7 in [numbers]")
else:
    print("7 not in [numbers]")

#task2

animals = ("pies", "kot", "ryba")
print(type(animals))

if "kot" in animals:
    print("'kot' in (animals)")
else:
    print("'kot' not in (animals)")

#task3

user = { "name": "Jan", "age" : 35 }

if "name" in user:
    print("OK")
else:
    print("NOK")

name = user.get("name", "Unknown")
print(name)



