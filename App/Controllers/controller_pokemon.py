"""
Aqui é onde vamos receber as nossas APIs e os REQUESTs
"""
import requests
import pprint
#Primeiro objetivo é pegar as informações basicas e necessárias de um pokemon.

def test_name_id(pokemon):
    url_pokemon=f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    req_url = requests.get(url_pokemon).json()
    return req_url['id']


def test_id_name(id):
    url_pokemon=f'https://pokeapi.co/api/v2/pokemon/{id}'
    req_url = requests.get(url_pokemon).json()
    return req_url['name']


def search_pokemon():
    global pokemon
    pokemon = str(input("Pokemon: "))
    res =f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    api=requests.get(res)
    global poke
    poke=api.json()
    #poke_info()


def get_weight():
    global poke
    print(f"Weight: {poke['weight']}")


def show_abilities():
    global poke
    print(f"Abilities: {[a['ability']['name'] for a in poke['abilities']]}")#Listcomprehensions


def show_types():
    global poke
    print(f"Type(s): {[t['type']['name'] for t in poke['types']]}")#Listcomprehensions


def show_evolutions():    
    global poke
    list_evolves = []
    evolves = poke['species']['url']
    get_evolves = requests.get(evolves).json()
    all_evolves = get_evolves['evolution_chain']['url']
    get_all_evolves = requests.get(all_evolves).json()
    names_evolves = get_all_evolves['chain']
    while names_evolves:
        list_evolves.append(names_evolves['species']['name'])
        names_evolves = names_evolves['evolves_to'][0] if names_evolves['evolves_to'] else None
    print(f"As evoluções do seu pokemon são às : {' -> ' .join(list_evolves)}")
   

def show_battle_infos():
    global poke
    if 'pokemon' in globals():
        stats = poke['stats']
        #abilities = poke['abilities'].json()

        print(f"Essas são as informações de batalha do seu Pokemon:\n")
        for stat in stats:
            print(f"{stat['stat']['name']} = {stat['base_stat']}" )