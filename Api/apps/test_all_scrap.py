from Api.apps.all_scrap import *


def test_get_data():
    assert type(get_data()) == str
    assert 'html' in get_data()

def test_get_elements():
    assert type(get_elements()) == tuple
    assert len(get_elements()) == 2

def test_get_games():
    assert type(get_games()) == list
    assert len(get_games()) > 0
    assert [['timestamp', 'time', 'sport', 'country', 'fixture'] for _ in get_games()[0].keys()]

def test_get_links():
    assert type(get_links()) == list
    assert len(get_links()) > 0
    assert [['title', 'link'] for _ in get_links()[0].keys()]


def test_add_links():
    assert type(add_links()) == list
    assert len(add_links()) > 0
    assert [['timestamp', 'time', 'sport', 'country', 'fixture', 'links'] for _ in add_links()[0].keys()]


def test_games():
    assert games() == "\tUse argument 'help' for more info."
    assert games('help') == "\tUse argument 'json' to get json format. \n\tUse argument 'dict' to get dictionary format. \n\tUse argument 'save' to save data in database."
    assert type(games('dict')[0]) == dict
    assert type(games('dict')) == list
    assert type(games('json')) == str
    assert [['timestamp', 'time', 'sport', 'country', 'fixture', 'links'] for _ in games('dict')[0].keys()]
    assert len(games('dict')[0]['links']) > 0




