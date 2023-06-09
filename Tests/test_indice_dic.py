import requests
import pprint

"""
def test_name_id(pokemon):
    url_pokemon=f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    req_url = requests.get(url_pokemon).json()
    return f"Your name is: {req_url ['name']}"


def test_id_name(id):
    url_pokemon=f'https://pokeapi.co/api/v2/pokemon/{id}'
    req_url = requests.get(url_pokemon).json()
    return f"Your ID is: {req_url['id']}"
"""



def test_name_or_id(id_name):
    url_pokemon=f'https://pokeapi.co/api/v2/pokemon/{id_name}'
    req_url = requests.get(url_pokemon).json()
    if isinstance(req_url['key']) == int:
        return f"Your ID is: {req_url['id']}"
    elif isinstance(req_url['key']) == str:
        return f"Your name is: {req_url ['name']}"
    else:
        return 'Pokemon not found'


print(test_name_or_id(25))