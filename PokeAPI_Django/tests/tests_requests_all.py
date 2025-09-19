import requests

def all_pokemons():
    url = "https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0."
    all_pokemons = requests.get(url).json()

    poke = {
        "name":[p['name'] for p in all_pokemons['results']],
        }
    
    for keys, value in poke.items():
        return keys, value



a = all_pokemons()
print(a)