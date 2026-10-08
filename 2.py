punkty = int(input("Podaj liczbę punktów: "))

if punkty >= 0 and punkty <= 49:
    ocena = "2.0"
elif punkty >= 50 and punkty <= 59:
    ocena = "3.0"
elif punkty >= 60 and punkty <= 60:
    ocena = "3.5"
elif punkty >= 70 and punkty <= 79:
    ocena = "4.0"
elif punkty >= 80 and punkty <= 89:
    ocena = "4.5"
elif punkty >= 90 and punkty <= 100:
    ocena = "5.0"
else:
    ocena = "Podaj prawidlowa ilosc punktow"

print(f"Uzyskana ocena: {ocena}")