czas_parkowania = int(input("Podaj czas parkowania(h): "))
if czas_parkowania <= 1:
    kwota = 1
elif czas_parkowania > 1 and czas_parkowania <= 3:
    kwota = 12
elif czas_parkowania > 3 and czas_parkowania <= 6:
    kwota = 20
elif czas_parkowania >= 6:
    kwota = 30
else:
    kwota = "Niepoprawne dane"

print(F"Czas postoju: {czas_parkowania}")
print(F"Oplata za parking: {kwota}")