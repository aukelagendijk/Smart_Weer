import weerstation
import smart_controller
import weer_online

def main():
    while True:
        print("1. Weerstation")
        print("2. Smart Controller")
        print("3. Huidig weer Utrecht")
        print("4. Stoppen")

        keuze = input("Maak een keuze: ")

        if keuze == "1":
            weerstation.weerstation()

        elif keuze == "2":
            smart_controller.smart_app_controller()

        elif keuze == "3":
            print(f"De huidige temperatuur in Utrecht is {weer_online.huidig_weer()}°C")

        elif keuze == "4":
            print("Programma gestopt.")
            break

        else:
            print("Ongeldige keuze.")


main()
