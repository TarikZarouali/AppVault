# Import functions from other files
from raad_het_nummer import raad_het_nummer
from dagboek import dagboek_menu

# Function to display the app logo
def toon_logo():
    logo = r"""
      _____                  ____   ____            .__   __   
  /  _  \ ______ ______   \   \ /   /____   __ __|  |_/  |_ 
 /  /_\  \\____ \\____ \   \   Y   /\__  \ |  |  \  |\   __\
/    |    \  |_> >  |_> >   \     /  / __ \|  |  /  |_|  |  
\____|__  /   __/|   __/     \___/  (____  /____/|____/__|  
        \/|__|   |__|                    \/                 
                                                     
    """
    print(logo)

# Hoofdmenu
def toon_menu():
    while True:
        print("\nWelkom bij de app vault! Maak een keuze:")
        print("========================================")
        print("1. Raad het nummer spel")
        print("2. Dagboek")
        print("3. Stop")
        print("========================================")

        keuze = input("Voer je keuze in (1-3): ")

        if keuze == "1":
            raad_het_nummer()
        elif keuze == "2":
            dagboek_menu()
        elif keuze == "3":
            print("Bedankt voor het spelen!")
            break
        else:
            print("Ongeldige keuze, probeer opnieuw.")

# Start het programma met het logo en hoofdmenu
if __name__ == "__main__":
    toon_logo()
    toon_menu()
