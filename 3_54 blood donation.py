
age = 18
weight = 49

if age >= 18 and weight >= 50:
        print("blood donation condition ok")
else:
    print("blood donation condition Nok")
    if age < 18: print("under 18 age")
    if weight < 50: print("under 50 weight")

print( )

age = 18
weight = 50

if age >= 18:
    if weight >= 50:
        print("Może oddać krew")
    else:
        print("Nie można oddać krwi, za niska waga")
else:
    print("Nie można oddać krwi, za mały wiek")