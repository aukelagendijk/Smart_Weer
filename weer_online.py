import requests

def huidig_weer():
    url = "https://api.open-meteo.com/v1/forecast?latitude=52.09&longitude=5.12&current=temperature_2m"

    response = requests.get(url)
    gegevens = response.json()

    temperatuur = gegevens["current"]["temperature_2m"]
    return temperatuur

