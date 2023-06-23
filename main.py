from pojistovna import Pojistovna

def main():
    pojistovna = Pojistovna("Pojistovna Programatoru")
    print("------------------------")
    print("Evidence pojistenych")
    print("------------------------\n")
    # 1 - novy pojisteny, 2 - vypsat pojistene
    # 3 - vyhledat pojisteneho, 4 - konec
    akce = None
    informace_akce = "Vyberte si akci:\n1 - Pridat noveho pojisteneho\n2 - Vypsat vsechny pojistene\n3 - Vyhledat pojisteneho\n4 - Konec\n"
    while True:
        akce = input(informace_akce)
        print(akce)

        if akce == "1":
            jmeno = input("Zadejte jmeno pojisteneho:\n")
            prijmeni = input("Zadejte prijmeni:\n")
            vek = input("Zadejte vek:\n")
            telefon = input("Zadejte telefonni cislo:\n")
            pojistovna.pridat_pojisteneho(jmeno, prijmeni, vek, telefon)
            print("Data byla ulozena.")
        elif akce == "2":
            pojistovna.vypsat_pojistene()
        elif akce == "3":
            jmeno = input("Zadejte jmeno pojisteneho:\n")
            prijmeni = input("Zadejte prijmeni:\n")
            pojistovna.vyhledat_pojisteneho(jmeno, prijmeni)
        elif akce == "4":
            print("Aplikace Pojistovna se vypina...")
            exit()
        else:
            print(f"Neplatna akce '{akce}', zadejte prosim nejakou akci z vyberu.")

main()