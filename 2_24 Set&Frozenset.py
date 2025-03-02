
setData = {2000,3000,1,4,5}

print(setData)
print(sorted(setData))

setData.add(22)
print(type(setData))
print( )

for v in setData:
    print(v)

print( )


frozenData = frozenset(sorted(setData))
print(frozenData)

for v in frozenData:
    print(v)

print( )