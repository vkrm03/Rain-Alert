import requests
from twilio.rest import Client

end_point = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "api_key"
account_sid = "AC6e4319ea1e1407400c9f41db89c5d000"
auth_token = "a180971b9a3c27a1a9edb4a0cc8fcee1"
client = Client(account_sid, auth_token)

WEATHER_PARA = {
    "lat":9.336825522469725,
    "lon":77.43038330857543,
    "appid":api_key,
    "exclude":"current,minutely,daily"
}

response = requests.get(end_point, params=WEATHER_PARA)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_is_rain = False

for hour in weather_slice:
    code = int(hour["weather"][0]["id"])
    if code < 700:

        will_is_rain = True

if will_is_rain:
    message = client.messages.create(
        body="today is mostly cloudy or mostly rainy day",
        from_='+14048003273',
        to='+918903468604'
    )
else:
    print("sms")
