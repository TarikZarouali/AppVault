# Functie om het dagboekbestand te lezen
def lees_dagboek_bestand():
    try:
        with open("dagboek.txt", "r") as f:
            entries = [regel.strip().split(";") for regel in f.readlines()]
            return {entry[0]: entry[1] for entry in entries}
    except FileNotFoundError:
        return {}

# Functie om de inhoud van het dagboek te lezen
def lees_dagboek_inhoud():
    try:
        with open("inhoud_dagboek.txt", "r") as f:
            inhoud = [regel.strip().split(";") for regel in f.readlines()]
            return {entry[0]: entry[1:] for entry in inhoud if entry[1:]}  
    except FileNotFoundError:
        return {}

# Functie om de inhoud van het dagboek bij te werken
def schrijf_dagboek_inhoud(inhoud):
    with open("inhoud_dagboek.txt", "w") as f:
        for naam, items in inhoud.items():
            if items: 
                f.write(f"{naam};{';'.join(items)}\n")

# Functie om het dagboekbestand bij te werken
def schrijf_dagboek_bestand(entries):
    with open("dagboek.txt", "w") as f:
        for naam, code in entries.items():
            f.write(f"{naam};{code}\n")

# Functie om een nieuw dagboek toe te voegen
def voeg_dagboek_toe():
    dagboek_entries = lees_dagboek_bestand()

    naam = input("Voer de naam van je dagboek in: ")
    if naam in dagboek_entries:
        print("Er bestaat al een dagboek met deze naam. Kies een andere naam.")
        return

    code = input("Voer een code voor dit dagboek in: ")
    dagboek_entries[naam] = code
    schrijf_dagboek_bestand(dagboek_entries)
    print("Dagboek toegevoegd!")

# Functie om een nieuw dagboek item toe te voegen
def voeg_dagboek_item_toe():
    dagboek_entries = lees_dagboek_bestand()
    dagboek_inhoud = lees_dagboek_inhoud()

    naam = input("Voer de naam van je dagboek in: ")
    if naam not in dagboek_entries:
        print("Geen dagboek gevonden met deze naam.")
        return

    code = input("Voer de code van dit dagboek in: ")
    if dagboek_entries[naam] == code:
        entry = input("Voer je dagboek item in: ")
        if naam in dagboek_inhoud:
            dagboek_inhoud[naam].append(entry)
        else:
            dagboek_inhoud[naam] = [entry]
        schrijf_dagboek_inhoud(dagboek_inhoud)
        print("Dagboek item toegevoegd!")
    else:
        print("Verkeerde code, toegang geweigerd.")

# Functie om een dagboek item te verwijderen
def verwijder_dagboek_item():
    dagboek_entries = lees_dagboek_bestand()
    dagboek_inhoud = lees_dagboek_inhoud()

    naam = input("Voer de naam van je dagboek in: ")
    if naam not in dagboek_entries:
        print("Geen dagboek gevonden met deze naam.")
        return

    code = input("Voer de code van dit dagboek in: ")
    if dagboek_entries[naam] == code:
        if naam in dagboek_inhoud and dagboek_inhoud[naam]:
            print(f"Dagboek items voor '{naam}':")
            for index, item in enumerate(dagboek_inhoud[naam], start=1):
                print(f"{index}. {item}")

            item_nummer = int(input("Voer het nummer van het item in dat je wilt verwijderen: "))
            if 1 <= item_nummer <= len(dagboek_inhoud[naam]):
                verwijderd_item = dagboek_inhoud[naam][item_nummer - 1] 
                bevestiging = input(f"Ben je zeker dat je het item '{verwijderd_item}' wilt verwijderen? (y/n): ")
                if bevestiging.lower() == 'y':
                    dagboek_inhoud[naam].pop(item_nummer - 1) 
                    schrijf_dagboek_inhoud(dagboek_inhoud)  
                    print(f"Item '{verwijderd_item}' is verwijderd.")
                else:
                    print("Verwijdering geannuleerd.")
            else:
                print("Ongeldig nummer, probeer opnieuw.")
        else:
            print(f"Het dagboek '{naam}' is leeg.")
    else:
        print("Verkeerde code, toegang geweigerd.")

# Functie om een dagboek te verwijderen
def verwijder_dagboek():
 
    dagboek_entries = lees_dagboek_bestand()

    naam = input("Voer de naam van je dagboek in dat je wilt verwijderen: ")
    if naam in dagboek_entries:
        code = input("Voer de code van dit dagboek in: ")
        if dagboek_entries[naam] == code:
            bevestiging = input(f"Ben je zeker dat je het dagboek '{naam}' wilt verwijderen? (y/n): ")
            if bevestiging.lower() == 'y':
                del dagboek_entries[naam] 
                schrijf_dagboek_bestand(dagboek_entries) 
                dagboek_inhoud = lees_dagboek_inhoud()
                if naam in dagboek_inhoud:
                    del dagboek_inhoud[naam] 
                    schrijf_dagboek_inhoud(dagboek_inhoud) 
                print(f"Dagboek '{naam}' is verwijderd.")
            else:
                print("Verwijdering geannuleerd.")
        else:
            print("Verkeerde code, toegang geweigerd.")
    else:
        print("Geen dagboek gevonden met deze naam.")

# Functie om een dagboek te openen
"""
dit is een comment
"""
def open_dagboek():

    dagboek_entries = lees_dagboek_bestand()
    dagboek_inhoud = lees_dagboek_inhoud()

    naam = input("Voer de naam van je dagboek in: ")
    if naam not in dagboek_entries:
        print("Geen dagboek gevonden met deze naam.")
        return

    code = input("Voer de code van dit dagboek in: ")
    if dagboek_entries[naam] == code:
        if naam in dagboek_inhoud:
            print(f"Dagboek items voor '{naam}':")
            for item in dagboek_inhoud[naam]:
                print(f"- {item}")
        else:
            print(f"Het dagboek '{naam}' is leeg.")
    else:
        print("Verkeerde code, toegang geweigerd.")

# Submenu voor dagboek
def dagboek_menu():
    while True:
        print("\nDagboek opties:")
        print("1. Dagboek toevoegen")
        print("2. Dagboek item toevoegen")
        print("3. Dagboek openen")
        print("4. Dagboek item verwijderen")
        print("5. Dagboek verwijderen")
        print("6. Terug naar hoofdmenu")

        keuze = input("Voer je keuze in (1-6): ")

        if keuze == "1":
            voeg_dagboek_toe()
        elif keuze == "2":
            voeg_dagboek_item_toe()
        elif keuze == "3":
            open_dagboek()
        elif keuze == "4":
            verwijder_dagboek_item()
        elif keuze == "5":
            verwijder_dagboek()
        elif keuze == "6":
            break
        else:
            print("Ongeldige keuze, probeer opnieuw.")
