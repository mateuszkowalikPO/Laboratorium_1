pierwsza_liczba = int(input("Podaj pierwsza liczbe: "))
druga_liczba = int(input("Podaj druga liczbe: "))
if pierwsza_liczba > druga_liczba:
    print("Pierwsza liczba musi byc mniejsza od drugiej")
    exit()
for i in range(pierwsza_liczba, druga_liczba + 1):
    if i % 2 == 0:
        print(f"{i} - Parzysta")
    else:
        print(f"{i} - Nieparzysta")