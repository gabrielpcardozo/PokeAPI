
""" 
Nesse arquivo quero criar todas as funcoes NATIVAS fora da API.

A ideia desse meu arquivo é criar os meus serviços onde vamos apresentar
    Treinador
    Pokemons
    inventário
"""
from ..Controllers import controller_pokemon

treinadores = {}

class Pokemon:
    def __init__(self,name, type):
        self.name = name
        self.type = type


class Treiner:

    xp = 0

    def __init__(self,name, nickname):
        self.name = name
        self.nickname = nickname
        self.bag = {
            'pokebolas':[],
            'Pokedex':{'pokemons':[]}
            },
        self.insignia = []
        Treiner.xp = self.xp


    def create_trainer(name, nick):
        #name = input('Qual o seu nome?\n').title()
        #nick = input('\nqual o seu nome de treinador?').title()
        append_trainers = treinadores['Treinador'] = name
        append_nick = treinadores['nickname'] = nick
        return append_trainers, append_nick


    def capture_pokemon():
        pass


    def add_poke():
        add_poke = controller_pokemon.Pokemon.id_name(10)        
        pass


persona_1 = Treiner.create_trainer('gabriel','ash')
print(persona_1)