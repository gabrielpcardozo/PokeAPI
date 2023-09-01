""" 
Aqui é mais um teste para pegar o pokemon direto da API e não criar uma lista com um numero X.
Base é o vídeo -> https://www.youtube.com/watch?v=jKpbmq67a4c
"""
import requests
"""

def search_pokemon():
    global pokemon
    pokemon = str(input("Pokemon: "))
    res =f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    api=requests.get(res)
    global poke
    poke=api.json()
    info_poke(poke)

def info_poke(poke):
    for i in poke['abilities']:
        print(i['ability']['name'])



search_pokemon()
"""
def search_pokemon():
    pokemon = str(input("Pokemon: "))
    res = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    api = requests.get(res)
    
    if api.status_code == 200:
        poke = api.json()
        abilities = [ability['ability']['name'] for ability in poke['abilities']]
        
        for ability in abilities:
            get_ability_damage(ability)
    else:
        print("Erro ao obter os dados do Pokémon.")

def get_ability_damage(ability_name):
    ability_api = f'https://pokeapi.co/api/v2/ability/{ability_name}'
    ability_api_json = requests.get(ability_api).json()
    
    if 'effect_entries' in ability_api_json:
        effect_entries = ability_api_json['effect_entries']
        
        for entry in effect_entries:
            if entry['language']['name'] == 'en':
                effect = entry['effect']
                print(f'Damage of {ability_name}: {effect}')
                break
        else:
            print(f'Could not find information for {ability_name}.')
    else:
        print(f'Could not find information for {ability_name}.')

search_pokemon()
