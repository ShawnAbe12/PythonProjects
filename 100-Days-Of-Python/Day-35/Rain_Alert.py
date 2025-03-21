import requests
from twilio.rest import Client
import os


account_SID = "ACf94a2f699832425e79e33226b4c0388c"
auth_token = "3a10d181f21db58524b58eef6da8c3d1"

api_key = "2dc61cd6197e82f72d802b2eef1f3e29"

LAT = 33.034061
LNG = -97.079643
api_endpoint = "https://api.openweathermap.org/data/2.5/forecast?q=Lewisville&APPID=2dc61cd6197e82f72d802b2eef1f3e29"
weather_parameters = {
    "lat": LAT,
    "lon":LNG,
    "appid":api_key,
    "cnt":4

}
connection = requests.get(url=api_endpoint, params=weather_parameters)
connection.raise_for_status()
will_rain = False
data = connection.json()["list"]
for w_data in data:
    if int(w_data["weather"][0]["id"]) < 700:
        will_rain = True

if will_rain or True:
    client = Client(account_SID, auth_token)
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='You need a Umbrella Today',
        to='whatsapp:+19723458736'
    )

    print(message.status)
# description = weather["description"]
# if int(weather) < 700:
#     print()
# print(data,weather)