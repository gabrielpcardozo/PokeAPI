#Make same tests with a damage
import requests

def search_pokemon():
    global pokemon
    pokemon = str(input("Pokemon: "))
    res =f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    api=requests.get(res)
    global poke
    poke=api.json()

def get_ability_damage(ability_name):
    ability_api = f'https://pokeapi.co/api/v2/ability/{ability_name}'
    ability_api_json = requests.get(ability_api).json()
    effect_entries = ability_api_json['effect_entries']
    
    for entry in effect_entries:
        if entry['language']['name'] == 'en':
            effect = entry['effect']
            print(f'Damage of {ability_name}: {effect}')
            break
    else:
        print(f'Could not find information for {ability_name}.')

# Exemplo de uso:
ability_name = 'blaze'
get_ability_damage(ability_name)


teste = get_ability_damage('torrent')
print(teste)