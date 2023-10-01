""" 
Nesse arquivo quero criar todas as funcoes NATIVAS fora da API.

A ideia desse meu arquivo é criar os meus serviços onde vamos apresentar
    Treinador
    Pokemons
    inventário
"""
import time
start_time = time.time()
import sys
sys.path.insert(0, '/home/gcardozo/Projects/Python/PokeAPI/App/Controllers')
import controller_pokemon
import requests

treinadores = []
pokedex = []

#Realizar diversas chamadas ao site do pokeAPI não está dando certo sendo retornado pelo controller.PokeAPI()get_mmain_pokemon() error 404 diversas vezes. sendo possível um limite de somente uma instância.
#Vou repaginar a classe para realizarmos menos chamadas. Vou manter essa classe salva na pasta de Tests.


"""name_api = None

if url == 200:
    okemon_data = requests.get(url).json()
print("pNot found.")
"""
class Pokemon: 

    xp = 0
    level = 0
    infos = {}

    def __init__(self,search_pokemon):
        url = f'https://pokeapi.co/api/v2/pokemon/{search_pokemon}'
        poke = requests.get(url).json()
        
        #Main infos
        self.__name = poke['name']
        self.__id = poke['id']
        self.__type = [t['type']['name'] for t in poke['types']]
        #Stats
        self.__hp = poke['stats'][0]['base_stat']
        self.__attack = poke['stats'][1]['base_stat']
        self.__defense = poke['stats'][2]['base_stat']
        self.__especialatt = poke['stats'][3]['base_stat']
        self.__especialdef = poke['stats'][4]['base_stat']
        self.__speed = poke['stats'][5]['base_stat']
        #Combat
        self.__abilities = [a['ability']['name'] for a in poke["abilities"]]

    def __str__(self):
        infos = {
                "Main infos":{
                    "Name":self.__name,
                    "ID":self.__id,
                    "Type":self.__type,
                },
                "Stats":{
                    "HP":self.__hp,
                    "Attack":self.__attack,
                    "Defense":self.__defense,
                    "Special-Attack":self.__especialatt,
                    "Special-Defense":self.__especialdef,
                    "Speed":self.__speed
                },
                "Abilities":{
                    'Abilities':self.__abilities
                }
                 }
        return str(infos)
    
    def show_id(self):
        return self.id

    def evolution():
        """
        Aqui eu quero fazer um sistema de evolução dos pokemons, vou precisar contabilizar o XP
        de cada POKEMON e vou precisar também de algum item ou um situação no jogo. 
        """
        pass


    def infos_battle(self):
        infos = [
        controller_pokemon.CollectInfos().collect_attack(self.name),
        controller_pokemon.CollectInfos().collect_defense(self.name)
        ]
        return infos


class Trainer:

    xp = 0

    def __init__(self,name, nickname):
        self.name = name
        self.nickname = nickname
        self.bag = {
            'pokeballs':{'Pokeballs':0, 'Masterballs':0},
            'Pokedex':pokedex
            },
        self.insignia = []
        Trainer.xp = self.xp


    def add_trainer(self,name):
        treinadores.append(name)


    def __str__(self):
        return f"Nome do treinador: {self.name}, seu apelido é: {self.nickname},\n Pokeballs: {self.bag[0]['pokeballs']}, \n Seus pokemons são os {str(self.bag[0]['Pokedex'])}"

    def name_instance(self):
        return self.name

    def add_pokeballs(self, pokeball, amount):
       if pokeball == 'pokeball':
        self.bag[0]['pokeballs']['Pokeballs'] = amount
       elif pokeball == 'masterball':
           self.bag[0]['pokeballs']['Masterballs'] = amount
       else:
           return "Pokebolla não encontrada"
           
    def show_pokeball(self):
        return f"Você possui {self.bag[0]['pokeballs']} Pokeballs."

    def capture_pokemon():
        pass

    def add_pokemons(self,name_pokemon):
        self.bag[0]['Pokedex'].append(str(name_pokemon))

    def show_my_pokemons(self):
        return f"Esses são os seus Pokemons: {str(self.bag[0]['Pokedex'])}"
        
    def inventory():
        pass


test = Pokemon('pikachu')
print(test)

end_time = time.time()
execution_time = end_time - start_time
# Mostrar o tempo em minutos
tempo_em_minutos = execution_time
print(f"Tempo de execução: {tempo_em_minutos:.2f} segundos")