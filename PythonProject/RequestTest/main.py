import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '03451c37d3b1af905dcaa4e0bb9a606b'
HEADER = {'Content-Type' : 'application/json','trainer_token': TOKEN}
body_new_pokemon = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_change = {
    "pokemon_id": "204195",
    "name": "Фунтик",
    "photo_id": 7
}

pokemon_in_pokebol = {
    "pokemon_id": "204203"
}


response_create = requests.post(url=f'{URL}/pokemons',headers = HEADER,json = body_new_pokemon)
print(response_create.text)

change_pokemon = requests.put(url = f'{URL}/pokemons',headers = HEADER,json = body_change)
print(change_pokemon.text)

catch_in_pokebol = requests.post(url=f'{URL}/trainers/add_pokeball',headers=HEADER,json = pokemon_in_pokebol)
print(catch_in_pokebol.text)


