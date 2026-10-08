temperatura_pomieszczenia = int(input("Podaj temperatura pomieszczenia: "))
czy_ktos_w_pomieszczeniu = input("Czy ktos w pomieszczeniu(tak/nie): ")
czy_okno_otwarte = input("Czy okno otwarte(tak/nie): ")

if czy_ktos_w_pomieszczeniu == "tak":
    ogrzewanie = "WYLACZONE"
    powod = "brak"
elif czy_okno_otwarte == "nie" and czy_ktos_w_pomieszczeniu == "tak" and temperatura_pomieszczenia < 20:
    ogrzewanie = "WLACZONE"
    powod = "20 C"
elif czy_okno_otwarte == "nie" and czy_ktos_w_pomieszczeniu == "nie" and temperatura_pomieszczenia < 16:
    ogrzewanie = "WLACZONE"
    powod = "16 C"
else:
    ogrzewanie = "WYLACZONE"
    powod = "brak"

print(f"Ogrzewanie: {ogrzewanie}")
print(f"Tempertur poniezej: {powod}")