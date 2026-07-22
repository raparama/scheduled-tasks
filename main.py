import os
import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
# api_key     = '5a3ca956e59bc0ce51f9706c453d7811'
# account_sid = 'AC7a291e5c8b7bb6e9a47b254b202f7125'
# auth_token  = '8a9a2ce4a971dd06626f9dfa2f49960e'
api_key     = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
weather_params = {
    "lat"   :   19.075983,
    "lon"   :   72.877655,
    "appid" :   api_key,
    "cnt"   :   4
}

response = requests.get(url=OWM_Endpoint, params=weather_params)
print(response.status_code)
response.raise_for_status()
weather_data = response.json()
print(weather_data)
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+12603006548',
        body="It's going to rain 🌧️ today. Remember to bring an ☔️",
        to='+919962025865'
    )
    print(message.sid)

