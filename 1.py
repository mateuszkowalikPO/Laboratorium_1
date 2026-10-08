cena_produktu = int(input("Podaj cene: "))
liczba_zamawianych = int(input("Podaj liczba zamawianych: "))
cena_laczna = cena_produktu * liczba_zamawianych

if (cena_laczna > 100):
    koszt_dostawy = 0
else:
    koszt_dostawy = 12


print(f"Do zapłaty: {cena_laczna + koszt_dostawy}")
