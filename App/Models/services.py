""" 
Nesse arquivo quero criar todas as funcoes NATIVAS fora da API.

A ideia desse meu arquivo é criar os meus serviços onde vamos apresentar
    Treinador
    Pokemons
    inventário
"""
import sys
sys.path.insert(0, '/home/gcardozo/Projects/Python/PokeAPI/App/Controllers')
import controller_pokemon


treinadores = []
pokedex = []

#Realizar diversas chamadas ao site do pokeAPI não está dando certo sendo retornado pelo controller.PokeAPI()get_mmain_pokemon() error 404 diversas vezes. sendo possível um limite de somente uma instância.
#Vou repaginar a classe para realizarmos menos chamadas. Vou manter essa classe salva na pasta de Tests.

class Pokemon: 

    xp = 0

    def __init__(self, pokemon_name):
        #about pokemon api
        self.name = controller_pokemon.ShowInfos().show_name(pokemon_name)
        self.id = controller_pokemon.ShowInfos().show_id(pokemon_name)
        #Cacracters
        self.type = controller_pokemon.ShowInfos().show_type(pokemon_name)
        self.weight =  controller_pokemon.ShowInfos().show_weight(pokemon_name)
        #Combat
        self.hp = controller_pokemon.ShowInfos().show_HP(pokemon_name)
        self.abilities = controller_pokemon.ShowInfos().show_abilities(pokemon_name)
        self.attack = controller_pokemon.ShowInfos().show_attack(pokemon_name)
        self.defense = controller_pokemon.ShowInfos().show_defense(pokemon_name)
        self.super_attack = controller_pokemon.ShowInfos().show_special_attack(pokemon_name)
        self.super_defense = controller_pokemon.ShowInfos().show_special_defense(pokemon_name)
        self.speed = controller_pokemon.ShowInfos().show_speed(pokemon_name)
    
    def add_pokedex(self, pokemon_name):
        pokedex.append(pokemon_name)

    
    def show_my_pokemons():
        for p in pokedex:
            print(p)


    def evolution():
        """
        Aqui eu quero fazer um sistema de evolução dos pokemons, vou precisar contabilizar o XP
        de cada POKEMON e vou precisar também de algum item ou um situação no jogo. 
        """
        pass


    def infos():
        """
        Aqui vai ser a função de informações da pokedex, onde vamos printar
        todas as evoluções dos pokemons.
        """
        pass



class Trainer:

    xp = 0

    def __init__(self,name, nickname):
        self.name = name
        self.nickname = nickname
        self.bag = {
            'pokeballs':{'Pokeballs':0, 'Masterballs':0},
            'Pokedex':[]
            },
        self.insignia = []
        Trainer.xp = self.xp


    def add_trainer(self,name):
        treinadores.append(name)


    def __str__(self):
        return f"Nome do treinador: {self.name}, seu apelido é: {self.nickname},\n Pokeballs: {self.bag[0]['pokeballs']},\n Seus pokemons são os {self.bag[0]['Pokedex']}"

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
        self.bag[0]['Pokedex'].append(name_pokemon)


    def show_my_pokemons(self):
        return self.bag[0]['Pokedex']

    def inventory():
        pass