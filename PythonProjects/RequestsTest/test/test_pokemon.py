import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json'}

def test_get_trainers():
    response = requests.get(url=f'{URL}/trainers', params={'level': 1}, timeout=5)
    assert response.status_code == 200, 'Unexpected status code'

def test_get_trainer_id():
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id': 3769}, timeout=5)
    assert response.status_code == 200, 'Unexpected status code'
