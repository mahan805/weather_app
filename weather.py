import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"

    response = requests.get(url)

    data = response.json()

    temperature = data["current_condition"][0]["temp_C"]

    return temperature