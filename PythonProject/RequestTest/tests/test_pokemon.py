import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '03451c37d3b1af905dcaa4e0bb9a606b'
HEADER = {'Content-Type' : 'application/json','trainer_token': TOKEN}
TRAINER_ID = '18831'

def test_status_code():
    response = requests.get(url= f'{URL}/pokemons',params = {'trainer_id': TRAINER_ID}) 
    assert response.status_code == 200