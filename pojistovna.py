
# Třída PojistenaOsoba obsahuje informace o pojištěné osobě
class PojistenaOsoba:
    def __init__(self, jmeno, prijmeni, vek, mobile_num):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.mobile_num = mobile_num

    def __str__(self):
        return f"Jméno: {self.jmeno}, Příjmení: {self.prijmeni}, Věk: {self.vek}, Mobilní číslo: {self.mobile_num}"


# Třída EvidencePojisteni obsahuje funkce pracující se seznamem pojištěných osob
class EvidencePojisteni:
    def __init__(self):
        self.pojisteni_seznam = []

    def vlozeni_pojisteneho(self, pojistena_osoba):  # Funkce slouží pro vložení pojištěného (na konec seznamu)
        self.pojisteni_seznam.append(pojistena_osoba)
        print(f"Pojistená osoba {pojistena_osoba.jmeno} {pojistena_osoba.prijmeni} byla úspěšně přidána.")

    def vyhledani_pojisteneho(self, jmeno, prijmeni):  # Funkce slouží k hledání pojištěného podle jména a příjmení
        nalezeni = [pojistena_osoba for pojistena_osoba in self.pojisteni_seznam
                    if pojistena_osoba.jmeno.lower() == jmeno.lower()
                    and pojistena_osoba.prijmeni.lower() == prijmeni.lower()]
        if nalezeni:
            for pojistena_osoba in nalezeni:
                print(str(pojistena_osoba))
        else:
            print(f"Pojistená osoba s jménem {jmeno} {prijmeni} nebyla nalezena.")

    def vypis_vsech_pojistenych(self):  # Funkce slouží k výpisu záznamů všech pojištěných
        if self.pojisteni_seznam:
            for pojistena_osoba in self.pojisteni_seznam:
                print(str(pojistena_osoba))
        else:
            print("Evidence pojistění je prázdná.")