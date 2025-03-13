
#identity operators

strData = "test"

print( "dir(strData):",dir(strData))

print( "strData.upper():",strData.upper())

intData = 10
print( "dir(intData):",dir(intData))

print( )

a = [1,2,3]
b = a

print( "a is b:",a is b)
print( )

a.append(4)
print("a.append(4)")
print("print(a):",a)
print("print(b):",b)
print("a is not b:", a is not b )
print( )

c = [3,4,5]

print(" a is c:",a is c )
print(" a is not c:",a is not c )