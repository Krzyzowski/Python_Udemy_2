
a = 1
b = 2

print("id: a =",id(a))

print("id: b =",id(b))

print("id(a) = id(b)", id(a)==id(b) )
print( )


a = 1
addr1 = id(a)
print("addr1 =", addr1)


a += 1
addr2 = id(a)
print("addr2 =", addr2)

print("addr1 = addr2:", addr1==addr2)
print( )

#addr3 &4
print("float:")
f = 3.2
addr3 = id(f)
f= f + 2.5
addr4 = id(f)

print("addr3:", addr3)
print("addr4:", addr4)
print("addr3 == addr4: ", addr3 == addr4)
print( )

#addr5 & 6

print("string:")
s = "Hello"
addr5 = id(s)

s = s + " world!"
addr6 = id(s)

print("addr5:", addr5)
print("addr6:", addr6)
print("addr5 == addr6:",addr5==addr6)
print( )

#addr 7 & 8
print(tuple)
t = (0,1,2,3)
addr7 = id(t)

t = t + (4,5)
addr8 = id(t)

print("addr7:", addr7)
print("addr8:", addr8)
print("addr7 == addr8:", addr7 == addr8)

print("list")
#addr 9 & 10

listData = ['a', 'b']
addr9 = id(listData)

listData += ['c', 'd']
addr10 = id(listData)
print("addr9 == addr10:", addr9==addr10)
print( )

print("set")
#addr 11 & 12
setData = {5,6}

addr11 = (id(setData))
setData.add(7)
print(setData)
addr12 = id(setData)

print("addr11:",addr11 )
print("addr12:",addr12)
print("addr11 == addr12:", addr11 == addr12)
print( )


print("dict")
#addr 13 & 14
dictData = {"a":0, "b":1}
addr13 = id(dictData)
dictData["c"] = 2
print("dictData a b c:", dictData)
addr14 = id(dictData)

print("addr13:",addr13)
print("addr14:",addr14)









