
numbers = [7,8,9,10,11,12 ]
print("typ numbers:", type(numbers))
print("numbers:",numbers)
print( )

tupleNumbers = tuple(numbers)
print("typ tupleNumbers: ", type(tupleNumbers))
print("tupleNumbers:", tupleNumbers)
print( )

mixedList = ["Ola", 232, 232.232,  ]
print("type mixedList: ", type(mixedList))
print("mixedList: ", mixedList)
print( )

setMixed = set(mixedList)
print("type setMixed:", type(setMixed))
print("setMixed:", setMixed)

setNumbers = set(tupleNumbers)
print("type setNumbers:", type(setNumbers))
print("setNumbers: ", setNumbers)
print( )
frozenSetNumbers = frozenset(setNumbers)
print("type frozenSetNumbers:", type(frozenSetNumbers))
print("frozenSetNumbers :", frozenSetNumbers)
print( )

nameAgePairs =(("Ola", 23 ),("Marek", 24 ))
print("type nameAgePairs:", type(nameAgePairs))
print("nameAgePAirs: ", nameAgePairs)
print( )
ageDict = dict(nameAgePairs)
print("type ageDict: ", type(ageDict))
print("ageDict: ", ageDict )
