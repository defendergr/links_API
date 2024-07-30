from fastapi.encoders import jsonable_encoder

from Api import app
from Api.apps import games
from Api.env import *
import requests

from geopy.geocoders import Nominatim
from fastapi.responses import JSONResponse
from datetime import datetime


@app.get('/')
def home():
    text = 'sport links, search machine API v1 By Defender'
    return text

@app.get('/links')
def get_links():
    data = jsonable_encoder(games('dict'))
    return JSONResponse(data)

@app.get('/football')
def get_football():
    url = "https://sofascores.p.rapidapi.com/v1/events/schedule/date"
    today = datetime.today().strftime("%Y-%m-%d")

    querystring = {"sport_id": "1", "date": today}

    headers = {
        "X-RapidAPI-Key": SOFA_API_KEY,
        "X-RapidAPI-Host": "sofascores.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    json_data = response.json()
    all_matches_data = []
    tournaments = ["Serie A", "LaLiga", "Ligue 1", "Bundesliga", "Premier League"] #TODO pull from db

    for key in (json_data["data"]):
        match_data = {}
        league = key['tournament']['name']

        if [x for x in tournaments if x == league]:
            match_data['category'] = league
            match_data['startTimeStamp'] = key['startTimestamp']
            match_data['tournament'] = league
            match_data['teams'] = f"{key['homeTeam']['name']} - {key['awayTeam']['name']}"
            if "current" in key["homeScore"]:
                match_data['score'] = f"{key['homeScore']['current']}-{key['awayScore']['current']}"

            all_matches_data.append(match_data)

    return JSONResponse(all_matches_data)


def user_location(locating):
    geolocator = Nominatim(user_agent="WeatherApp")

    location = geolocator.geocode(locating)

    latitude = location.latitude
    longitude = location.longitude

    # print("The latitude of the location is: ", location.latitude)
    # print("The longitude of the location is: ", location.longitude)
    return {"lat":latitude, "long":longitude}
