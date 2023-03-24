from Api import app


@app.get('/')
def home():
    text = 'sport links search machine API By Defender'
    return text

@app.get('/links')
def get_links():
    gameList = 'test'
    return gameList
