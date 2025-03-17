
# 1

number = 5
while number >0:
    #number -= 1
    print(number)
    number -= 1

print( )
# 2

number = 1
while number < 6:
    #number += 1
    print(number)
    number += 1

num = 0
while True:
    print("Wprawdź liczbę lub 'q' aby aby zakończyć:")
    strData = input()
    if strData == "q" : break
    num += int(strData)
    print("Wartość po dodaniu liczby: " + str(num))

print( )

num = 0
while True:
    print("Wprowadź liczbę lub 'exit', aby zakończyć:")
    strData = input()
    if strData.lower() == "exit":
        break
    try:
        num += int(strData)
        print("Wartość po dodaniu liczby: " + str(num))
    except ValueError:
        print("Proszę wprowadzić poprawną liczbę.")
