import time as t
from mujslovnik import slovnik

#úvod
print("Vítejte na filmové stránce Legalni.Filmy.CZ")
t.sleep(2)

jmeno = str(input("Zadejte jméno: "))
prijmeni = str(input("Zadejte příjmení: "))
celejmeno = f"{jmeno} {prijmeni}"
t.sleep(2)

volba = str(input("\nZadejte zda chcete Filmy, Seriály nebo Plán: "))

#SpatnyVyber
while volba not in slovnik:
    print("Je nám líto, ale tuto službu neposkytujeme")
    volba = str(input("Zadejte zda chcete Filmy, Seriály nebo Plán: "))
    t.sleep(0.5)

#Filmy
if volba == "Filmy":
    volbazanru = str(input("Zadejte jaký chcete žánr (Válečné, Komedie, Horrory nebo Dětské): "))
    if volbazanru in slovnik["Filmy"]:
        for oznacenimovie, movie in slovnik[volba][volbazanru].items():
            print(f"{oznacenimovie} {movie}")

#Seriály
if volba == "Seriály":
    volbazanru2 = str(input("Zadejte jaký chcete žánr (Válečné, Komedie, Horrory nebo Dětské): "))
    if volbazanru2 in slovnik["Seriály"]:
        for oznaceniserialu, serial in slovnik[volba][volbazanru2].items():
            print(f"{oznaceniserialu} {serial}")

#Plán
if volba == "Plán":

    print("""Zvolil jste Plán, v následujícím odstavci 
vám porovnáme Standart, Pro a Ultra""")
    input("zmáčkněte enter pro pokračování: ")
    print("""  
        
Standart
-cena: 0kč/měsíc
-možnost sledování filmů zdarma s reklamami
-možnost mít rozkoukané až 3 seriály/filmy
          
Pro
-cena: 290kč/měsíc
-možnost přeskakovat reklamy po 3 sekundách
-možnost mít rozkoukaných až 5 seriálů/filmů
          
Ultra
-cena: 450kč/měsíc
-užijte si svůj oblíbený film/seriál úplně bez reklam
-možnost mít rozkoukaný libovolný počet seriálů/filmů
-k nově nahraným filmům/seriálům budete mít 
 přístup o 7 dní dříve než ostantí
          
""")

    volbaplanu = str(input("Zadejte jaký chcete plán: "))

    if volbaplanu == "Standart":
        print(f"\nZvolili jste Standart, přejeme vám příjemnou zábavu (s reklamami) {celejmeno}")
    if volbaplanu == "Pro":
        print("\nZvolil jste Pro")
        print(f"přejememe vám příjemnou zábavu {celejmeno}")
    if volbaplanu == "Ultra":
        print("\nZvolili jste Ultra (nejlepší volba)")
        print(f"přejememe vám příjemnou zábavu {celejmeno}")




