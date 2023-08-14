from Api import app
from Api.apps import allScrap
import requests
import orjson
from geopy.geocoders import Nominatim
from fastapi.responses import JSONResponse, ORJSONResponse



@app.get('/')
def home():
    text = 'sport links, search machine API v1.1.2 By Defender'
    return text

@app.get('/links')
def get_links():
    gameList = allScrap()
    return gameList

@app.get('/weather')
def get_weather():
    url = "https://forecast9.p.rapidapi.com"

    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "forecast9.p.rapidapi.com"
    }

    # API Documentation
    # settingsAPI = "https://tapi.wetter.com/v2.3/documentation/assertible.json"
    # response = requests.get(settingsAPI, headers=headers)
    # weather = response.json()

    location = user_location("Thessaloniki, Greece")

    latitude = round(location["lat"], 5) # 40.64031
    longitude = round(location["long"], 5) # 22.93527

    hourly = f"/rapidapi/forecast/{latitude}/{longitude}/hourly/"

    response = requests.get(url+hourly, headers=headers)

    return response.json()

    # return weather["paths"]["/rapidapi/forecast/{latitude}/{longitude}/hourly/"]["get"]["summary"]



def user_location(locating):
    geolocator = Nominatim(user_agent="WeatherApp")

    location = geolocator.geocode(locating)

    latitude = location.latitude
    longitude = location.longitude

    # print("The latitude of the location is: ", location.latitude)
    # print("The longitude of the location is: ", location.longitude)
    return {"lat":latitude, "long":longitude}
