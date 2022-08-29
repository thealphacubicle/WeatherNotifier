import requests,os
from Location import Location
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from dotenv import load_dotenv

location_coordinates = Location.get_latitude_longitude(self=Location(address="9 Frying Pan Alley, London E1 7HS, United Kingdom",country = "United Kingdom"))
MY_LAT = location_coordinates[0]
MY_LONG = location_coordinates[1]
load_dotenv("/Users/srihariraman/Desktop/Python Bootcamp/python-bootcamp/Project: Weather Notifier/env.env")
#proxy_client = TwilioHttpClient(proxy={'http': os.environ['http_proxy'], 'https': os.environ['https_proxy']})
OPENWEATHER_APP_ID = os.getenv("OPENWEATHER_APP_ID")
ACCT_SID = os.getenv("ACCT_SID")
AUTH_TKN = os.getenv("API_KEY")

params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": OPENWEATHER_APP_ID,
    "units": "imperial"
}
request = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=params)
request.raise_for_status()
weather_data = request.json()

def recommend_precipitation_gear(current_weather_id):
    if "2" in current_weather_id:
        return "Thunderstorm expected. You need an umbrella and a raincoat!"
    elif "3" in current_weather_id:
        return "Drizzle expected. You may need an umbrella!"
    elif "5" in current_weather_id:
        return "Substantial rain expected. You need an umbrella and a raincoat!"
    elif "6" in current_weather_id:
        return "Snow expected. You need an umbrella, raincoat, and snow boots!"
    elif "7" in current_weather_id:
        return "Heavy rain expected. You need an umbrella and a raincoat!"
    else:
        return "No preparatory gear needed."

def send_message(precipitation_message_to_send):
    #client = Client(ACCT_SID, AUTH_TKN, http_client=proxy_client)
    client = Client(ACCT_SID, AUTH_TKN,)
    message = client.messages.create(
        body=precipitation_message_to_send,
        from_='17372587257',
        to='+13026857938'
    )
    return message.status


#TODO: Get the current weather data and check to see if temperature minimum is less than the personal limit
current_weather_id = str(weather_data["weather"][0]["id"] / 100) #Div by 100 to get first digit
message_status = send_message(recommend_precipitation_gear(current_weather_id))