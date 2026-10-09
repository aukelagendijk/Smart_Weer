def aantal_dagen(inputFile):
    try:
        bestand = open(inputFile, "r")
        regels = bestand.readlines()
        bestand.close()

        aantal = len(regels) - 1
        return aantal

    except FileNotFoundError:
        print("Het bestand is niet gevonden.")
        return 0

def auto_bereken(inputFile, outputFile):
    try:
        bestand = open(inputFile, "r")
        regels = bestand.readlines()
        bestand.close()

    except FileNotFoundError:
        print("Het bestand is niet gevonden.")
        return False

    uitvoer = open(outputFile, "w")

    for regel in regels[1:]:
        delen = regel.split()

        datum = delen[0]
        aantal_personen = int(delen[1])
        setpoint = float(delen[2])
        buitentemperatuur = float(delen[3])
        neerslag = float(delen[4])

        verschil = setpoint - buitentemperatuur

        if verschil >= 20:
            cv = 100
        elif verschil >= 10:
            cv = 50
        else:
            cv = 0

        ventilatie = aantal_personen + 1
        if ventilatie > 4:
            ventilatie = 4

        if neerslag < 3:
            bewatering = True
        else:
            bewatering = False

        uitvoer.write(f"{datum};{cv};{ventilatie};{bewatering}\n")

    uitvoer.close()

    return True


def overwrite_settings(outputFile):
    datum = input("Welke datum wil je aanpassen? ")

    try:
        bestand = open(outputFile, "r")
        regels = bestand.readlines()
        bestand.close()

    except FileNotFoundError:
        print("Het bestand is niet gevonden.")
        return

    datum_gevonden = False
    nieuwe_regels = []

    for regel in regels:
        delen = regel.strip().split(";")

        if delen[0] == datum:
            datum_gevonden = True

            systeem = input("Welk systeem wil je aanpassen? 1: CV, 2: ventilatie, 3: bewatering: ")

            if systeem not in ["1", "2", "3"]:
                return -3

            waarde = input("Wat is de nieuwe waarde? ")

            if systeem == "1":
                if not waarde.isdigit() or int(waarde) < 0 or int(waarde) > 100:
                    return -3
                delen[1] = waarde

            elif systeem == "2":
                if not waarde.isdigit() or int(waarde) < 0 or int(waarde) > 4:
                    return -3
                delen[2] = waarde

            elif systeem == "3":
                if waarde == "0":
                    delen[3] = "False"
                elif waarde == "1":
                    delen[3] = "True"
                else:
                    return -3

            regel = ";".join(delen) + "\n"

        nieuwe_regels.append(regel)

    if datum_gevonden == False:
        return -1

    bestand = open(outputFile, "w")
    bestand.writelines(nieuwe_regels)
    bestand.close()

    return 0


def smart_app_controller():
    inputFile = "input.txt"
    outputFile = "output.txt"

    while True:
        print("1. Aantal dagen")
        print("2. Actuatoren automatisch berekenen")
        print("3. Instelling aanpassen")
        print("4. Stoppen")

        keuze = input("Maak een keuze: ")

        if keuze == "1":
            aantal = aantal_dagen(inputFile)
            print(f"Aantal dagen: {aantal}")

        elif keuze == "2":
            if auto_bereken(inputFile, outputFile) == True:
                print("De instellingen zijn berekend.")

        elif keuze == "3":
            resultaat = overwrite_settings(outputFile)

            if resultaat == 0:
                print("De instelling is aangepast.")
            elif resultaat == -1:
                print("Datum niet gevonden.")
            elif resultaat == -3:
                print("Ongeldige keuze of waarde.")

        elif keuze == "4":
            print("Programma gestopt.")
            break

        else:
            print("Ongeldige keuze.")

