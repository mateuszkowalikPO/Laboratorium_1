wiek = int(input("Podaj wiek: "))

if wiek < 18:
    zgoda_opiekuna = input("Czy masz zgode opiekuna?(tak/nie): ")

dokument_tozsamosci = input("Czy masz dokument tozsamosci?(tak/nie): ")

wypozyczenie_mozliwe = "Wypozyczenie mozliwe"
wypozyczenie_niemozliwe = "Wypozyczenie niemozliwe"

if wiek >= 18 and dokument_tozsamosci == "tak":
    print(wypozyczenie_mozliwe)
elif wiek <= 17 and wiek >= 13 and zgoda_opiekuna == "tak" and dokument_tozsamosci == "tak":
    print(wypozyczenie_mozliwe)
elif wiek < 13:
    print(wypozyczenie_niemozliwe)
else:
    print(wypozyczenie_niemozliwe)