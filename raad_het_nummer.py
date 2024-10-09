from random import randint

def raad_het_nummer():
    print("Welkom bij het spel 'Raad het nummer'!")
    print("Please enter your name")
    playerName = input()

    theNumber = randint(1, 100)

    for totalGuesses in range(5):
        guessedNumber = int(input(f"Hi {playerName}, raad het nummer van 1 tot 100: "))

        if guessedNumber < theNumber:
            print("Je gok is lager dan het juiste nummer.")
        elif guessedNumber > theNumber:
            print("Je gok is hoger dan het juiste nummer.")
        else:
            print("Gefeliciteerd! Je hebt het juiste nummer geraden.")
            print(f"Het duurde je {totalGuesses + 1} pogingen!")
            break
    else:
        print(f"Ah jammer, je hebt geen pogingen meer... Het juiste nummer was: {theNumber}")