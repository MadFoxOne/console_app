# Načtení externího souboru pojistovna.py
from pojistovna import PojistenaOsoba, EvidencePojisteni


def main():
    evidence = EvidencePojisteni()
    # Výběr možností (Menu)
    while True:
        print("\n----------------------------------------")
        print("Evidence pojištěných")
        print("----------------------------------------\n")
        print("Vyberte si akci:")
        print("1 - Přidat nového pojistného")
        print("2 - Vypsat všechny pojištěné")
        print("3 - Vyhledat pojistného")
        print("4 - Konec")

        volba = input()
        # Vložení nového pojištěného
        if volba == "1":
            jmeno = input("Zadejte jméno pojistného: ")
            if not jmeno:  # Ochrana proti prázdnému zadání
                print("Jméno nesmí být prázdné.")
                continue

            prijmeni = input("Zadejte příjmení: ")
            mobile_num = input("Zadejte telefonní číslo: ")
            vek = int(input("Zadejte věk: "))

            pojistena_osoba = PojistenaOsoba(jmeno, prijmeni, vek, mobile_num)
            evidence.vlozeni_pojisteneho(pojistena_osoba)

        elif volba == "2":  # Volba pro kompletní výpis seznamu
            evidence.vypis_vsech_pojistenych()

        elif volba == "3":  # Volba pro hlednání v seznamu podle jména a příjmení
            jmeno_hledani = input("Zadejte jméno a příjmení pojistného k vyhledání: ")
            jmeno, prijmeni = jmeno_hledani.split()
            evidence.vyhledani_pojisteneho(jmeno, prijmeni)

        elif volba == "4":  # Ukončení programu
            print("Konec programu.")
            break

        else:  # Ochrana proti neplatné volbě
            print("Neplatná volba.")


if __name__ == "__main__":
    main()
