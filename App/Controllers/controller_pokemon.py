"""
A ideia aqui é ter duas Classes 
    class PokeAPI
        A ideia dessa classe é ficar com as funções de comunicação com os REQUESTS
    class PokemonShow
        A idea dessa classe é conter as informações de publicação para o usuário final.

    class PokemonChange
        Estou pensando em criar uma para manter as alterações e preparar dados para uso caso precise.
"""
import requests
import pprint

#A ideia dessa classe é Termos toda a nossa comuinição com o PokeAPI é realizarmos todos os gets com o site, para utilizamos.
class PokemonAPI:
    def __init__(self):
        self.abilities_effect = {}

    def get_main_pokemon(self, pokemon_name):
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
        #url = f'http://127.0.0.1:5000/pokemon//{pokemon_name}' #Testes utilizando o flask para tentar não tomar alguns bloqueios. 
        response = requests.get(url)
        req = response.status_code
        #return response
        if req >= 200:
            return response.json()
        else:
            print(f"Erro na solicitação: {response.status_code}")


    def get_infos_battle(self, battle_infos_hp):
        collect_battle_infos = PokemonAPI().get_main_pokemon(battle_infos_hp)
        stats = collect_battle_infos['stats']
        infos_battle = {}

        for stat in stats:
            stat_name = stat['stat']['name']
            base_stat = stat['base_stat']
            infos_battle[stat_name] = base_stat
        return infos_battle
#infos_battle é um função de coleta das informações de batalha dos pokemons.
#Exemplo.     
#{'hp': 35, 'attack': 55, 'defense': 40, 'special-attack': 50, 'special-defense': 50, 'speed': 90}
    def get_infos_envolves(self, pokemon_name):
        collect_evolves = PokemonAPI().get_main_pokemon(pokemon_name)
        
        if 'species' in collect_evolves:
            species_url = collect_evolves['species']['url']
            species_response = requests.get(species_url)
            species_data = species_response.json()
        
            if 'evolution_chain' in species_data:
                evolution_chain_url = species_data['evolution_chain']['url']
                evolution_chain_response = requests.get(evolution_chain_url)
                evolution_chain_data = evolution_chain_response.json()
                return evolution_chain_data
    
    def get_abilities(self, pokemon_name):
        get_pokemon = PokemonAPI().get_main_pokemon(pokemon_name)
        get_abilities = get_pokemon["abilities"]
        for a in get_abilities:
            ability_name = a['ability']['name']
            effect_name = a['ability']['url']

            u = requests.get(effect_name).json()
            entry = u["effect_entries"]

            for i in entry:
                if i["language"]["name"] == "en":
                    ability_effect = i["short_effect"]
                    break
            else:
                ability_effect = "No English description available"

            self.abilities_effect[ability_name] = ability_effect

        return self.abilities_effect

#A ideia dessa classe é deixar os saídas mais apropriadas para serem mostradas para os usuários ou até mesmo utilizadas.
class CollectInfos:
    def collect_name(self, name):
        collect_name = PokemonAPI().get_main_pokemon(name)
        if collect_name is not None:
            return collect_name['name']
        else:
            return None

    def collect_id(self, id):
        collect_id = PokemonAPI().get_main_pokemon(id)
        return collect_id['id']

    def collect_weight(self, weight):
        collect_weight = PokemonAPI().get_main_pokemon(weight)
        return collect_weight['weight']

    def collect_abilities(self, abilities):
        get_abilities = PokemonAPI().get_abilities(abilities)
        details = []
        for a, e in get_abilities.items():
            details.append(f"Habilidade: {a} -> Effect: {e}")
        
        return "\n".join(details)
    

    def collect_type(self,types):
        collect_type = PokemonAPI().get_main_pokemon(types)
        return f"Type(s): {[t['type']['name'] for t in collect_type['types']]}"#Listcomprehensions
  
    def collect_evolutions(self, pokemon_name):    
        collect_evolves = PokemonAPI().get_infos_envolves(pokemon_name)
                
    
        evolution_names = []
        chain = collect_evolves['chain']

        while chain:
            evolution_names.append(chain['species']['name'])
            chain = chain['evolves_to'][0] if chain.get('evolves_to') else None
                
        if evolution_names:
            evolution_chain = ' -> '.join(evolution_names)
            return f"As evoluções do seu Pokémon são: {evolution_chain}"
            
        return "Não foi possível obter informações de evolução para esse Pokémon."
    

    """
    Aqui começa uma sequência de informações de batalha de cada pokemon
    HP | ATTACK | DEFENSE | SPECIAL-ATTACK | SPECIAL-DEFENSE | SPEED
    Essas são as informações encontradas no PokeAPI.
    """
    def collect_HP(self, battle_infos_hp):
        hp = PokemonAPI().get_infos_battle(battle_infos_hp)
        return f" HP:{hp['hp']}" 

    def collect_attack(self, battle_infos_attack):
        attack = PokemonAPI().get_infos_battle(battle_infos_attack)
        return f" Attack:{attack['attack']}" 
    
    def collect_defense(self, battle_infos_defense):
        attack = PokemonAPI().get_infos_battle(battle_infos_defense)
        return f" Defense:{attack['defense']}"
    
    def collect_special_attack(self, battle_infos_special_attack):
        attack = PokemonAPI().get_infos_battle(battle_infos_special_attack)
        return f" Special Attack:{attack['special-attack']}"

    def collect_special_defense(self, battle_infos_special_defense):
        attack = PokemonAPI().get_infos_battle(battle_infos_special_defense)
        return f" Special Defense:{attack['special-defense']}"
        
    def collect_speed(self, battle_infos_speed):
        attack = PokemonAPI().get_infos_battle(battle_infos_speed)
        return f" Speed:{attack['speed']}"
    #Aqui acaba as informações de batalha.
    
    def collect_picture(self, picture):
        collect_picture = PokemonAPI().get_main_pokemon(picture)
        return collect_picture['sprites']['front_default']


list_pokedex = []

class Pokemon:
    def __init__(self, pokemon_name):
        self.name = collectInfos().collect_name(pokemon_name)

    def add_poke(poke):
        new_instance = Pokemon(poke)
        list_pokedex.append(new_instance)


#print(PokemonAPI().get_main_pokemon('pikachu'))
#print(collectInfos().collect_name('pikachu'))