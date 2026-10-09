def Fahrenheit(temp_celcius):
    temp_fahrenheit = 32 + 1.8 * temp_celcius
    return temp_fahrenheit

def gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid):
    gevoel = temp_celcius - luchtvochtigheid / 100 * windsnelheid
    return gevoel

def weerrapport(temp_celcius, windsnelheid, luchtvochtigheid):
    gevoel=gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid)
    if gevoel < 0 and windsnelheid > 10:
        return "Het is heel koud en het stormt! Verwarming helemaal aan!"
    elif gevoel < 0 and windsnelheid <= 10:
        return "Het is behoorlijk koud! Verwarming aan op de benedenverdieping!"
    elif 0 <= gevoel < 10 and windsnelheid > 12:
        return "Het is best koud en het waait; verwarming aan en roosters dicht!"
    elif 0 <= gevoel < 10 and windsnelheid <= 12:
        return "Het is een beetje koud, elektrische kachel op de benedenverdieping aan!"
    elif 10 <= gevoel < 22:
        return "Heerlijk weer, niet te koud of te warm."
    else:
        return "Warm! Airco aan!"

def weerstation():
    totaal_temperatuur = 0
    aantal_dagen = 0

    for dag in range(1, 8):
        while True:
            invoer_temp = input(f"Wat is op dag {dag} de temperatuur[C]: ")

            if invoer_temp == "":
                print("bye.")
                return

            try:
                temp_celcius = float(invoer_temp)
                break
            except ValueError:
                print("Voer een geldig getal in.")

        while True:
            invoer_wind = input(f"Wat is op dag {dag} de windsnelheid[m/s]: ")

            if invoer_wind == "":
                print("bye.")
                return

            try:
                windsnelheid = float(invoer_wind)
                break
            except ValueError:
                print("Voer een geldig getal in.")

        while True:
            invoer_vochtigheid = input(f"Wat is op dag {dag} de vochtigheid[%]: ")

            if invoer_vochtigheid == "":
                print("bye.")
                return

            try:
                luchtvochtigheid = int(invoer_vochtigheid)

                if 0 <= luchtvochtigheid <= 100:
                    break
                else:
                    print("Voer een getal tussen 0 en 100 in.")

            except ValueError:
                print("Voer een geldig geheel getal in.")

        totaal_temperatuur = totaal_temperatuur + temp_celcius
        aantal_dagen = aantal_dagen + 1

        gemiddelde = totaal_temperatuur / aantal_dagen

        print(f"Het is {temp_celcius}C ({Fahrenheit(temp_celcius)}F)")
        print(weerrapport(temp_celcius, windsnelheid, luchtvochtigheid))
        print(f"Gem. temp tot nu toe is {gemiddelde}")
        print("======================================")
