from django.shortcuts import render
from django.core.paginator import Paginator

import requests

def home(request):
    lucario ="https://pokeapi.co/api/v2/pokemon/lucario"
    get_lucario = requests.get(lucario).json()
    poke = {
        'name':get_lucario['name'],
        'id':get_lucario['id'],
        'type':[t['type']['name'] for t in get_lucario['types']],
        'HP': get_lucario['stats'][0]['base_stat'],
        'Attack': get_lucario['stats'][1]['base_stat'],
        'Defense': get_lucario['stats'][2]['base_stat'],
        'EspecialAttack':get_lucario['stats'][3]['base_stat'],
        'EspecialDefense':get_lucario['stats'][4]['base_stat'],
        'Speed': get_lucario['stats'][5]['base_stat'],
        'Abilities': [a['ability']['name'] for a in get_lucario["abilities"]],
        'Image': get_lucario['sprites']['back_default']
        }
    return render(request, "home.html", poke)

def all_pokemons(request):
    url = "https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0."
    all_pokemons = requests.get(url).json()
    #results = all_pokemons['results']

    
    poke = [p['name'] for p in all_pokemons['results']]

    paginator = Paginator(poke, 20)  # 20 pokemons por página
    page_number = request.GET.get("page")  # pega o número da página na URL ?page=2
    page_obj = paginator.get_page(page_number)

    return render(request, "all_pokemons.html", {"page_obj": page_obj})


