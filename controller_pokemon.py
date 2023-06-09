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


def poke_info():
    print('Aqui estão as informações do seu pokemon:\n')
    if pokemon in pokemon:
        pokemon_api = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'# Aqui colocamos a variavel no final da URL para realizar uma busca nas informacoes.
        pokemon_api_json = requests.get(pokemon_api).json()# como tudo se trata de formatos da WEB precisamos convertar todas as URLs para JSON.

       #Agora é necessário achar as evoluções do pokemon escolhido.
        specie_api = pokemon_api_json['species']['url']#Dentro da URL do POKEMON_API vai ter uma CHAVE especies e uma URL onde vao conter as caracteristicas dos pokemons.
        specie_api_json = requests.get(specie_api).json()# É necessário colocar tudo em .JSON
        
        evolution_api =  specie_api_json['evolution_chain']['url']# AQUI QUE A MAGICA ACONTECE PQP ISSO DEMOROU DEMAIS, as evolucoes estao nessa chave!!!!!!!!!!!PQPQ
        evolution_api_json = requests.get(evolution_api).json()# É necessário colocar tudo em .JSON
        
        #Agora a ideia aqui é pegar as evoluções e armazenar em algum lugar fora da URL.
        evolutions = []# tem que ser em lista pq tudo no python e lista
        essa_var_e_foda =evolution_api_json['chain']#Aqui vai ficar so os nomes das evolucoes
        
        while essa_var_e_foda:
            evolutions.append(essa_var_e_foda['species']['name'])#agora sao so os nomes das evolucoes na lista
            essa_var_e_foda = essa_var_e_foda['evolves_to'][0] if essa_var_e_foda['evolves_to'] else None #Aqui matamos o while como var = var toda vez que va[evolve][0] for diferente de None.
        #Informações do POKEMON.
        print(f"Name: {pokemon_api_json['name']}")
        print(f"Type(s): {[t['type']['name'] for t in pokemon_api_json['types']]}")#Listcomprehensions
        print(f"Abilities: {[a['ability']['name'] for a in pokemon_api_json['abilities']]}")#Listcomprehensions
        print(f"Weight: {pokemon_api_json['weight']}")
        print(f"As evoluções do seu pokemon são às: {' -> ' .join(evolutions)}") #Essa linha é uma brisa, ela concatena os elementos da lista com a seta ->
    else:
        print("Seu POKEMON não se ecnontra em nosso mundo.")


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


search_pokemon()

get_weight()