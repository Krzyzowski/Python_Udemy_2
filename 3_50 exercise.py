
#1

print("'firstName' + 'lastName' :", 'firstName' + 'lastName')

fullname = 'firstName' +' ' + 'lastName'
print("'firstName' + 'lastName':",fullname)
print( )

#2

listOne = [1,2,3]

listTwo = [4,5,6]

combinedList = listOne + listTwo
print("combinedList = listOne + listTwo:", combinedList)

#3

if len(combinedList) > 5:
    print("list too long")

#4


fullname = 'Chris Rea'
greeting = 'Hello' + ' ' + fullname

if 'Hello' in greeting:
    print(greeting)