cena_produktu = int(input("Podaj cena_produktu: "))
rabat_procent = int(input("Podaj rabat(%): "))


rabat = rabat_procent/100
kwota_rabatu = round(cena_produktu * rabat, 2)
cena_po_rabacie = cena_produktu - kwota_rabatu

print(f"\nCena poczatkowa: {cena_produktu} zl")
print(f"Kwota rabatu: {kwota_rabatu} zl")
print(f"Cena po rabacie: {cena_po_rabacie} zl")

if rabat_procent > 20:
    print("Duza promocja!")