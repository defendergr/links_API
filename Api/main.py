from Api import app
from Api.apps import allScrap

@app.get('/')
def home():
    text = 'sport links, search machine API v1.1.2 By Defender'
    return text

@app.get('/links')
def get_links():
    gameList = allScrap()
    return gameList
