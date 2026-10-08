wysokosc_choinki = int(input("Podaj wysokosc choinki: "))

for i in range(wysokosc_choinki):
    spacje = " " * (wysokosc_choinki - i - 1)
    gwiazdki = "*" * (2 * i + 1)
    print(spacje + gwiazdki)