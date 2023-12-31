
# Třída PojistenaOsoba obsahuje informace o pojištěné osobě
class PojistenaOsoba:
    def __init__(self, jmeno, prijmeni, vek, mobilni_cislo):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.mobilni_cislo = mobilni_cislo

    def __str__(self):
        return f"Jméno: {self.jmeno}, Příjmení: {self.prijmeni}, Věk: {self.vek}, Mobilní číslo: {self.mobilni_cislo}"


# Třída EvidencePojisteni obsahuje funkce pracující se seznamem pojištěných osob
class EvidencePojisteni:
    def __init__(self):
        self.pojisteni_seznam = []

    def vlozeni_pojisteneho(self, pojistena_osoba):  # Funkce slouží pro vložení pojištěného (na konec seznamu)
        self.pojisteni_seznam.append(pojistena_osoba)
        print("Data byla uložena. Pokračujte libovolnou klávesou... ")
        input()

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
