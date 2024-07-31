from fastapi.encoders import jsonable_encoder
from Api import app
from Api.apps import games
import os
import requests
from fastapi.responses import JSONResponse
from datetime import datetime

"""
Load the environment variables from the 'Api\env.py' file if it exists,
otherwise create the file with default values and load the environment variables.
"""
# Check if the 'Api\env.py' file exists
if os.path.isfile('Api\env.py'):
    # If the file exists, import the environment variables
    from Api.env import *
else:
    # If the file does not exist, create it with default values and import the environment variables
    with open('Api\env.py', 'w') as f:
        f.write("SOFA_API_KEY = ''")
    from Api.env import *


@app.get('/')
def home():
    """
        This route returns a simple text message.

        Returns:
            str: The text message.
        """
    text = 'sport links, search machine API v1 By Defender'
    return text


@app.get('/links')
def get_links():
    """
    Get the links data.

    Returns:
        JSONResponse: The JSON response containing the links data.
    """
    # Convert the games data to a JSON-serializable format
    data = jsonable_encoder(games('dict'))

    # Return the JSON response
    return JSONResponse(data)

@app.get('/football')
def get_football():
    """
    Retrieves football match data for today's matches from the Sofa Scores API.

    Returns:
        JSONResponse: A JSON response containing data about today's football matches.
    """
    # Check if SOFA_API_KEY is set
    if SOFA_API_KEY == '':
        return JSONResponse([{"error":"Sofa Scores API key not found", "solution":"Please set SOFA_API_KEY in env.py"}])

    # Set the URL and query parameters for the API request
    url = "https://sofascores.p.rapidapi.com/v1/events/schedule/date"
    today = datetime.today().strftime("%Y-%m-%d")
    querystring = {"sport_id": "1", "date": today}

    # Set the headers for the API request
    headers = {
        "X-RapidAPI-Key": SOFA_API_KEY,
        "X-RapidAPI-Host": "sofascores.p.rapidapi.com"
    }

    # Make the API request and get the response
    response = requests.get(url, headers=headers, params=querystring)
    json_data = response.json()

    # Initialize an empty list to store the match data
    all_matches_data = []

    # Define the list of tournaments to filter matches by
    tournaments = ["Serie A", "LaLiga", "Ligue 1", "Bundesliga", "Premier League"]

    # Iterate over the matches in the API response
    for key in (json_data["data"]):
        match_data = {}

        # Get the league name and check if it's in the list of tournaments
        league = key['tournament']['name']
        if [x for x in tournaments if x == league]:
            match_data['category'] = league
            match_data['startTimeStamp'] = key['startTimestamp']
            match_data['tournament'] = league
            match_data['teams'] = f"{key['homeTeam']['name']} - {key['awayTeam']['name']}"

            # Check if the match is currently in progress and get the score
            if "current" in key["homeScore"]:
                match_data['score'] = f"{key['homeScore']['current']}-{key['awayScore']['current']}"

            # Add the match data to the list
            all_matches_data.append(match_data)

    # Return the JSON response containing the match data
    return JSONResponse(all_matches_data)