
ileLiczb = int(input("Podaj, ile liczb chcesz wprowadzić: "))  # Konwersja na int
sum = 0
i = 0  # Inicjalizacja zmiennej i

while i < ileLiczb:
    liczba = int(input(f"Wprowadź liczbę {i + 1}: "))  # Pobierz liczbę i przekształć na int
    sum += liczba  # Dodaj liczbę do sumy
    i += 1  # Zwiększ licznik

srednia = sum / ileLiczb  # Oblicz średnią
print(f"Średnia wprowadzonych liczb wynosi: {srednia}")
