from django.shortcuts import render
import requests

url = "https://pokeapi.co/api/v2/"
first_get = requests.get(url)

lucario ="https://pokeapi.co/api/v2/pokemon/lucario"
get_lucario = requests.get(lucario)

def home(request):
    return render(request, "home.html", {})

def all_pokemons(request):
    lucario ="https://pokeapi.co/api/v2/pokemon/lucario"
    get_lucario = requests.get(lucario).json()
    poke = {
        'name':get_lucario['name'],
        'id':get_lucario['id'],
        'type':[t['type']['name'] for t in get_lucario['types']]
        }
    
    return render(request, "all_pokemons.html", poke)
