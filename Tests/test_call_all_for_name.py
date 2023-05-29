""" 
Aqui é mais um teste para pegar o pokemon direto da API e não criar uma lista com um numero X.
Base é o vídeo -> https://www.youtube.com/watch?v=jKpbmq67a4c
"""
import requests

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
