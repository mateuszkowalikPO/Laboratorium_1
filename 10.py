liczba_studentow = int(input("Podaj liczbe studentow: "))
zaliczeni = 0

for i in range(liczba_studentow):
    nazwisko = input(f"Nazwisko studenta {i + 1}: ")
    punkty = int(input(f"Punkty: "))
    if punkty >= 0 and punkty <= 49:
        ocena = 2.0
    elif punkty >= 50 and punkty <= 59:
        ocena = 3.0
    elif punkty >= 60 and punkty <= 69:
        ocena = 3.5
    elif punkty >= 70 and punkty <= 79:
        ocena = 4.0
    elif punkty >= 80 and punkty <= 89:
        ocena = 4.5
    elif punkty >= 90 and punkty <= 100:
        ocena = 5.0
    print(f"{nazwisko} - {punkty} pkt - {ocena}")
    if ocena > 3.0:
        zaliczeni += 1

print(f"Liczba studentow, ktorzy zaliczyli: {zaliczeni}")