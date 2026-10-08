odkladana_kwota = int(input("Ile odkladasz tygodniowo?: "))
liczba_tygodni = int(input("Przez ile tygodni?: "))
for i in range(liczba_tygodni):
    i += 1
    print(f"Tydzien {i}: {odkladana_kwota * i}")