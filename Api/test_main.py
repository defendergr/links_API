from fastapi.testclient import TestClient
from Api.main import app

client = TestClient(app)

def test_home():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == 'sport info API v1 By Defender'

def test_links():
    response = client.get('/links')
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'

def test_football():
    response = client.get('/football')
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'