odkladana_kwota = int(input("Ile odkladasz tygodniowo?: "))
liczba_tygodni = int(input("Przez ile tygodni?: "))
i = 1

for i in range(liczba_tygodni):
    print(f"Tydzien {i}: {odkladana_kwota * i}")
    i =+ 1

