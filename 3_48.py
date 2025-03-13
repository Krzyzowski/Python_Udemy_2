
#1

text = "Hello"
print("text.upper():",text.upper())
print( )
print("dir(text):",dir(text))
print( )

#2
x = 256
y = 256

print("x is y:", x is y)
print( )

#3

listOne =[0,1,2,3,4,5,6,7,8]
print("type(listOne):",type(listOne))
listTwo = listOne

print("listOne == listTwo:",listOne == listTwo)
print( )

#4

listOne.append(9)
print("listOne.append(9)",listOne)

if listOne == listTwo:
    print("listOne == listTwo:")

print( )
#5

listThree = listOne

if listOne == listThree:
    print("listOne == listThree:")