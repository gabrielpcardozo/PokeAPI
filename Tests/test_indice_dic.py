import requests
import pprint

"""var = requests.get('https://pokeapi.co/api/v2/pokemon/squirtle').json()
pprint.pprint(var)"""
def list_all_names():
    api = 'https://pokeapi.co/api/v2/pokemon/?limit=200'
    all_name = requests.get(api).json()
    pokemons = []
    for pokemon in all_name["results"]:
        pokemons.append(pokemon['name'])
    return pokemons


def poke_info():
    pokemon = input("Which POKEMON do you want information about? ")
    pokemons = list_all_names()  # get the list of all pokemon names
    print('Here is the information about your pokemon:\n')
    if pokemon in pokemons:
        # fetch the information about the pokemon from the API
        pokemon_api = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
        response = requests.get(pokemon_api).json()

        # fetch the evolution chain for the pokemon
        species_api = response['species']['url']
        species_response = requests.get(species_api).json()
        evolution_chain_api = species_response['evolution_chain']['url']
        evolution_chain_response = requests.get(evolution_chain_api).json()
        # extract the evolution chain from the response and print it out
        evolution_chain = []
        current = evolution_chain_response['chain']
        while current:
            evolution_chain.append(current['species']['name'])
            current = current['evolves_to'][0] if current['evolves_to'] else None
        print(f"Evolution chain: {' -> '.join(evolution_chain)}")

        # print the other information about the pokemon
        print(f"Name: {response['name']}")
        print(f"Type(s): {[t['type']['name'] for t in response['types']]}")
        print(f"Abilities: {[a['ability']['name'] for a in response['abilities']]}")
        print(f"Weight: {response['weight']}")
    else:
        print("Invalid pokemon name. Please try again.")

    
poke_info()