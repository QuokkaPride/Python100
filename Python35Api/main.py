import requests
from twilio.rest import Client
import os

API_KEY = os.environ.get("WEATHER_API_KEY")
ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"


account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

weather_params = {
    "lat": 42.346951,
    "lon": -71.547180,
    "cnt": 4,
    "appid": API_KEY,
    "units": "imperial",
}

response = requests.get(ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()

# first try
# for forecast in weather_data["list"]:
#     if forecast["weather"][0]["id"] < 700:
#         print("Bring Unbrella")
#         break
#     # print(forecast["weather"][0]["id"])


# more effcicient
if any(forecast["weather"][0]["id"] < 700 for forecast in weather_data["list"]):
    print("Bring an Umbrella")

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="+18775708016", body="Bring umbrella gurlie☔💃", to="+15087338486"
    )
    print(message.sid)

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_="whatsapp:+14155238886",
        content_sid="HXb5b62575e6e4ff6129ad7c8efe1f983e",
        content_variables='{"1":"12/1","2":"3pm"}',
        to="whatsapp:+15087338486",
    )

    print(message.sid)
