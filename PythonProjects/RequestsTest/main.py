"""
Pokemons sozdanie
"""

import requests

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json'}

body = {
    "trainer_token": "11c449b74368de6415e45aab23002778",
    "email": "Twilight20012000@mail.ru",
    "password": "Qwerty56789",
   }

response = requests.post(url=f'{URL}',json=body, headers=HEADER, timeout=5)
print(response)

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json'}
HEADER = {'trainer_token': '11c449b74368de6415e45aab23002778'}

body = {
    "name": "generate",
    "photo": "generate"
}

response = requests.post(url=f'{URL}/pokemons',json=body, headers=HEADER, timeout=5)

print(f'Статус код создания:{response.status_code}. Сообщение: {response.json()}')

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json'}
HEADER = {'trainer_token': '11c449b74368de6415e45aab23002778'}

body = {
    "pokemon_id": "28010",
    "name": "kapushka",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

response = requests.put(url=f'{URL}/pokemons',json=body, headers=HEADER, timeout=5)

print(f'Статус код обновления имени: {response.status_code}. Сообщение: {response.json()}')


URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json'}
HEADER = {'trainer_token': '11c449b74368de6415e45aab23002778'}

body = {
    "pokemon_id": "28010",
}

response = requests.post(url=f'{URL}/trainers/add_pokeball',json=body, headers=HEADER, timeout=5)

print(f'Статус код попадания в покебол: {response.status_code}. Сообщение: {response.json()}')