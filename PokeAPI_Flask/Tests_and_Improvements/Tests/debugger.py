"""
A ideia dessa arquivo é somente chamar as funções para ficar mais fácil com a tela splitada.
"""
import sys
import pprint
import requests

#variavel usada para testes. 
poke_test = 'snorlax'
#pprint -> Para retornos mais formatados.
pp = pprint.PrettyPrinter()
"""
Eu só consegui usar o 
pprint.print(conteudo)
de outra forma não conheço.
"""
######################
#Importação de MODULOS. 

"""
Aqui eu estou  importando os meus modulos para que eu consiga ter um arquivo para módulos.
"""
#Folder: App/Controller -> File:controller_pokemon.py
sys.path.insert(0, '/home/gcardozo/Projects/Python/PokeAPI/App/Controllers')
sys.path.insert(1, '/home/gcardozo/Projects/Python/PokeAPI/App/Models')
import controller_pokemon
import services
######################
#Testes para saber se os módulos estão funcionando.
#print(controller_pokemon.CollectInfos().collect_attack('pikachu'))
#print(controller_pokemon.CollectInfos().collect_id('pikachu'))

#trainer = services.Treiner.create_trainer("samuel","samuca")

###################################################################
##Aqui começam os testes!                                       ###
##Testes do módulo Controller_pokemon.                          ###
##Testes poara saber se a classe CollectInfos: está funcionando.### 
###################################################################
"""
#collect name
print(controller_pokemon.CollectInfos().collect_name(poke_test))
#collect_id
print(controller_pokemon.CollectInfos().collect_id(poke_test))
#get_weight
print(controller_pokemon.CollectInfos().collect_weight(poke_test))
#Type
print(controller_pokemon.CollectInfos().collect_type(poke_test))
#Evolves
print(controller_pokemon.CollectInfos().collect_evolutions(poke_test))
#abilities 
print(controller_pokemon.CollectInfos().collect_abilities(poke_test))
#Picture
print(controller_pokemon.CollectInfos().collect_picture(poke_test))

#Infos for battles
    #HP
print(controller_pokemon.CollectInfos().collect_HP(poke_test))
    #Attack
print(controller_pokemon.CollectInfos().collect_attack(poke_test))
    #Defense
print(controller_pokemon.CollectInfos().collect_defense(poke_test))
    #Special_Attack
print(controller_pokemon.CollectInfos().collect_special_attack(poke_test))
    #Special_Defense
print(controller_pokemon.CollectInfos().collect_special_defense(poke_test))
    #Speed
print(controller_pokemon.CollectInfos().collect_speed(poke_test))

"""
"""
#Esse foi o primeiro SUCESSO dos testes de CHEGAR no effects das habilidades.
dic = {}
for a in test_index:
    u = a['ability']['url']
    #print(u)
    #lista.append(u)
    u = requests.get(u).json()
    #pp.pprint(u)
    u = u["flavor_text_entries"]
    dic["teste_CHAVE"] = u[0]["flavor_text"]
    print(dic)
#Depois daqui foi só pra trás. 
    Inicialmente eu tentei criar duas funções umas para as HABILIDADES e outra
    para os efeitos. OBVIAMENTE não deu certo pois o dicionário que foi inicializado
    no __init__ não estáva conseguindo ler as duas funções corretamente, dito isso
    BURRO era obvio e não adiantava jogar em uma variavel pois deixaria de ser um dicionário "global"
    BURRO dnv. Entẽm era duas funções que estavam tentando se comunicar
    com o mesmo dicionário, até que me encheu o saco e eu comecei a testar tudo 
    em uma função mesmo!!!!! dito isso GENIO...(kk)
    Também acabei vendo na internet que tinha como filtrar por LINGUA que isso ajuda na hora de indexar.
No arquivo controller_pokemon.py na def get_abilities está a função funcionando.
aqui é só um resgistro do fracasso para nunca mais errar.
    def abilities
        for a in get_abilities:
            ability_name = a['ability']['name']
            self.abailities_effect[ability_name] = ""
        
        for a in get_abilities:
            u = a['ability']['url']
            #print(u)
            u = requests.get(u).json()
            u = u["flavor_text_entries"]
            self.abailities_effect = u[0]["flavor_text"]

        print(self.abailities_effect)

    def get_infos_effect_abilities(self, abilities):
        get_name = PokemonAPI().get_abilities(abilities)
        for i in get_name:
            u = i['ability']['url']
            print(u)
            u = requests.get(u).json()
            u = u["flavor_text_entries"]
            print(u)
            #self.abailities_effect[ability_name] = u[0]["flavor_text"]
            #effect = self.abailities_effect[ability_name]


print(controller_pokemon.PokemonAPI().get_abilities(pokemon))            

Alguimas coisas estão fora de contexto mas é só para armazenar as tentantivas e ter uma parâmetro de evolução.             

Oq eu estava retornando a def collect_abilities() 
#return f"Abilities: {[a['ability']['name'] for a in collect_abilities['abilities']]}"#Listcomprehensions

"""
####################################################################################
"""
Testes rápidos de batalhas, foi mais para enteder o index de cada coisa. 
def info_battle(battle):
    main_url = controller_pokemon.PokemonAPI().get_pokemon(battle)
    for stat in main_url['stats']:
        print(stat)

info_battle(pokemon)

print(controller_pokemon.PokemonAPI().infos_battle(pokemon))
"""

#######################################################
##Aqui começa os testes dos pokemons e do treinador.###
##folder:Model -> file:service                      ###
#######################################################

#local_test.add_pokedex()
#pokedex.append(local_test)
#local_test = 'pikachu'
#new_pokemon = services.Pokemon('pikachu')
#new_pokemon_one = services.Pokemon('squirtle')
#####################################
##Testes de instânica class Pokemon##
#####################################

"""first_pokemon = services.Pokemon(poke_test)
second_pokemon = services.Pokemon('lucario')
third_pokemon = services.Pokemon('palkia')
fourth_pokemon = services.Pokemon('totodile')
print(f"Aqui estamos utilizando o método __str__(): {first_pokemon.__str__()}")
print("############")
print(f"Aqui estamos utilizando o método __repr(): {first_pokemon.__repr__()}")
print("############")

#print(str(first_pokemon))
#print(services.Pokemon().name(first_pokemon))
first_trainer = services.Trainer('Gabriel', 'perigoso')
first_trainer.add_pokemons(first_pokemon)
first_trainer.add_pokemons(second_pokemon)
first_trainer.add_pokemons(third_pokemon)
first_trainer.add_pokemons(fourth_pokemon)
print(first_trainer)
print("############")
print(first_trainer.show_my_pokemons())
print("############")"""
#print(first_trainer.bag['Pokedex'].name)
#print(first_trainer.show_my_pokemons())

#new_pokemon.add_pokedex(new_pokemon)
#new_pokemon_one.add_pokedex(new_pokemon_one)

#print(services.Pokemon().collect_my_pokemons())

# print(services.pokedex)

#######################################################
##            Testes Classs Trainer                  ##
##                 Intancia 1.                       ##
##   Criação de intancias e população de inventário  ##
#######################################################

"""
treinador_1 = services.Trainer("Gabriel", "ash")
poke_1 = 'Lucario'
poke_2 = 'totodile'
poke_3 = 'Palkia'
treinador_1.add_pokemons(poke_1)
treinador_1.add_pokemons(poke_2)
treinador_1.add_pokemons(poke_3)
treinador_1.add_pokeballs('pokeball', 2)
treinador_1.add_pokeballs('masterball', 3)
######
#Testes de visualização.
#print(treinador_1)
treinador_1.add_trainer(treinador_1)
#print(services.treinadores)
#print(treinador_1.show_my_pokemons())
#print(treinador_1.show_pokeball())
print(treinador_1)

####################################
print("########################################")
####################################
#Instancia 2.
treinador_2 = services.Trainer("Samuel", "Brock")
poke_4 = 'Charmander'
poke_5 = 'Growlithe'
poke_6 = 'Mew'
treinador_2.add_pokemons(poke_4)
treinador_2.add_pokemons(poke_5)
treinador_2.add_pokemons(poke_6)
treinador_2.add_pokeballs('pokeball', 3)
treinador_2.add_pokeballs('masterball', 3)
treinador_2.add_trainer(treinador_2)
print(treinador_2)
####################################
print("########################################")
####################################
#Instancia 3.
treinador_3 = services.Trainer("Kaique", "Gary")
poke_7 = 'Snorlax'
poke_8 = 'Charizard'
poke_9 = 'Cindaquil'
treinador_3.add_pokemons(poke_7)
treinador_3.add_pokemons(poke_8)
treinador_3.add_pokemons(poke_9)
treinador_3.add_pokeballs('pokeball', 100)
treinador_3.add_pokeballs('masterball', 0)
treinador_3.add_trainer(treinador_3)
print(treinador_3)
"""

#######################################################
##            Testes Classs Pokemon                  ##
##                                                   ##
##   Criação de Pokemons e testes em suas chamadas   ##
#######################################################
"""
#Criar um pokemon
pokemon1 = services.Pokemon(poke_test)
print(pokemon1)
print(type(pokemon1))
print("##################")
print(pokemon1.show_id())
print(pokemon1.infos_battle())
"""
################################################################

#######################################################
##            Testes Classs Pokemon                  ##
##                                                   ##
##          Refatorteção da classe Pokemon           ##
#######################################################

test = services.Pokemon(poke_test)
print(test)


"""search_pokemon = poke_test
url = f'https://pokeapi.co/api/v2/pokemon/{search_pokemon}'
poke = requests.get(url).json()

pp.pprint(poke['stats'])
"""