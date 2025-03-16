#if
num = 4
if num > 5:
    print( str(num) + " większe od 5")
    if num >= 10:
        print( str(num) + " większe też od 10")
        if num > 20:
            print(str(num) +" większe też od 20" )
    print("ostatnie wcięcie if")

print("print niezależne od if")
print( )
#elif

num = 7
if num == 7:
    print("num jest 7")
elif num == 10:
    print("num jest 10")

print( )
#num = 20

num = 20

if num == 7:
    print(" num jest 7")
elif num == 10:
    print("num jest 10")
elif num == 12:
    print("num jest 12")
elif num == 14:
    print("num jest 14")
elif num >= 15:
    print("num jest większe równe 15")
print( )

#else

a = 10
b = 5

if a == b:
    print("a == b")
elif a < b:
    print("a < b")
else:
    print("a > b")

# oneliner :)

if a > b: print("in one line: a > b ")


