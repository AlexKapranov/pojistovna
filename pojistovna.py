from pojistenci import Pojistenec

class Pojistovna:
    """Reprezentuje pojistovnu - seznam jejich klientu a operace nad nimi."""
    seznam_pojistencu = []
    jmeno = None

    def __init__(self, jmeno):#
        self.jmeno = jmeno
        self.seznam_pojistencu = []

    def pridat_pojisteneho(self, jmeno, prijmeni, vek, telefon):
        self.seznam_pojistencu.append(Pojistenec(jmeno, prijmeni, vek, telefon))

    def vypsat_pojistene(self):
        print("------- Vypis pojistenych -------")
        if len(self.seznam_pojistencu) == 0:
            print("Zatim neexistuji zadni pojisteni.")
        else:
            for pojistenec in self.seznam_pojistencu:
                print(pojistenec)
        print("---------------------------------")

    def vyhledat_pojisteneho(self, jmeno, prijmeni):
        nalezen = False

        for pojistenec in self.seznam_pojistencu:
            if jmeno == pojistenec.jmeno and prijmeni == pojistenec.prijmeni:
                print(f"{pojistenec}\n")
                nalezen = True
                break

        if not nalezen:
            print(f"Nebyl nalezen zadny pojistenec s temito udaji: {jmeno} {prijmeni}")
