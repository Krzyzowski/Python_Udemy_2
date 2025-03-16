
while True:
    try:
        Age = int(input("Wpisz wiek psa (tylko liczby):"))
        #print(f"Wiek psa to: {Age} ")
        if Age <= 1 and Age > 0:
            dogAge = Age * 15
            print(f"Wiek psa w ludzkich latach to {dogAge}")
        elif Age <= 2 and Age > 1:
            dogAge = 15 +(Age - 1) * 9
            print(f"Wiek psa to {dogAge}")
        elif Age >2 and Age < 40:
            dogAge = 24 + (Age - 2) * 5
            print(f"Wiek psa w ludzkich latach to {dogAge}")
        else:
            print("Wiek psa jakiś magiczny")

        break # Exit the loop if the input is valid
    except ValueError:
        print("Błąd: Proszę wpisać tylko liczby. ")