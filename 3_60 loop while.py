


i = 0
sum = 0

while i <= 100:
    i += 1
    sum += i
    #print(i)

elif:
    print("koniec pętli while")

exept IndexError:

print("Suma liczb od 0 do 100:", sum)


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