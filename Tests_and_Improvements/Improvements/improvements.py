#Aqui todas as partes lentas e possíveis melhorias devem ser testadas e revisasdas aqui antes.
"""
Path -> App/Models/services.py
    Realizar melhorias de velocidade em nossa classe Pokemon.
"""
#Ela em conjunto com Classe PokeInfos do Path App/Controllers/controllers_pokemons.py estão sendo melhoradas juntas.
class Pokemon:

    xp = 0

    def __init__(self,pokemon_name):
        #A ideia aqui é deixar todas as informações salvas em um dicinário e só fazermos a indexação depois.
        base = controller_pokemon.PokeInfos().get_infos(pokemon_name)
        
        self.name = base['name']
        self.id = base['id']
        self.weight = base['weight']
        self.type = base['type']

#Como para instanciar cada informação dos pokemons está bloqueando o acesso do site vo criar um única chamada para todas as iformações.
class PokeInfos:
    def get_infos(self, poke_name):
        #Aqui seria a única chamada, dessa função tudo vai sair dela e vai passar por um dicionário.
        #Eestou fazendo dessa forma pois na Classe PokeAPI ela já trata a resposta 200 caso de erro. 
        data = PokemonAPI().get_main_pokemon(poke_name)
        #Tudo deve passar por um dicionário
        pokemon_infos = {
            "name": data['name'],
            "id": data["id"],
            "weight": data["weight"],
            "type": [t['type']['name'] for t in data['types']]
        }

        return pokemon_infos

""" 
A ideia com as duas classes a cima é deixar o fucionamento das requisições e comunicações com o PokeAPI.co mais rápidas sem bloqueios.
"""
############################################################