


listData = [1,2,3,4]
tupleData = tuple(listData)
print("tupleData:", tupleData)
print( )

tuple2 = ("Ola", "Adam")
newList = list(tuple2)
print("type newList:", type(newList))
print( )

listData = [1,2,3,1,2,5,6,7]
setData = set(listData)
print(type(setData))
print(setData)

frozensetData = frozenset(listData)
print(type(frozensetData))
print( )

tupleData = (("Adam", "adam#example.com"), ("Ola", "Ola#example.com" ))
dictData = dict(tupleData)
print(type(dictData))
print(dictData)
print(dictData["Adam"])


