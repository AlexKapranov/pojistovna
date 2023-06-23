class Pojistenec():
    """Reprezentuje pojisteneho v pojistovne."""
    jmeno = None
    prijmeni = None
    vek = None
    telefonni_cislo = 0

    def __init__(self, jmeno, prijmeni, vek, tel):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefonni_cislo = tel

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni} {self.vek} {self.telefonni_cislo}"
