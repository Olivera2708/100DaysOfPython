import requests

API_KEY = ""
LAT = 
LNG = 1

response = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall?lat={LAT}&lon={LNG}&exclude=current,daily,minutely&appid={API_KEY}")
response.raise_for_status()
data = response.json()

slice = data["hourly"][:12]
will_rain = False

for hour_data in slice:
    if int(hour_data["weather"][0]["id"]) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrela")
