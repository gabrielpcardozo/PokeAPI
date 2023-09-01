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
class PokemonAPI:
    def get_main_pokemon(self, pokemon_name):
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

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
            

class Pokemon:
    def name(self, poke_name):
        show_name = PokemonAPI().get_pokemon(poke_name)
        return show_name['name']

    def id(self, id):
        show_id = PokemonAPI().get_pokemon(id)
        return show_id['id']

    def weight(self, weight):
        show_weight = PokemonAPI().get_pokemon(weight)
        return show_weight['weight']

    def abilities(self, abilities):
        """show_abilities = PokemonAPI().get_main_pokemon(abilities)
        abilities_effects = {}
        
        for ability_data in show_abilities["abilities"]:
            ability_name = ability_data['ability']['name']
            ability_url = ability_data['ability']['url']
            ability_response = requests.get(ability_url).json()
            effect_entries = ability_response["effect_entries"]
            
            if effect_entries:
                short_effect = effect_entries[0]["short_effect"]
                abilities_effects[ability_name] = short_effect
        
        return abilities_effects"""
        
        """abilities =  show_abilities["abilities"]
        effects_data = show_abilities["abilities"]
        effects_data = effects_data['ability']['url']
        effects = effects_data.json()
        abilit_effec = {abilities['ability']['name'] : effects["effect_entries"]["short_effect"] for attack in effects_data}
        return  abilit_effec
        """
        #abilitAbilities: {[a['ability']['name'] for a in show_abilities['abilities']]}
        
        #return f"Abilities: {[a['ability']['name'] for a in show_abilities['abilities']]}"#Listcomprehensions

    def types(self,types):
        show_type = PokemonAPI().get_pokemon(types)
        return f"Type(s): {[t['type']['name'] for t in show_type['types']]}"#Listcomprehensions
  
    def evolutions(self, pokemon_name):    
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
    def HP(self, battle_infos_hp):
        hp = PokemonAPI().get_infos_battle(battle_infos_hp)
        return f" HP:{hp['hp']}" 

    def attack(self, battle_infos_attack):
        attack = PokemonAPI().get_infos_battle(battle_infos_attack)
        return f" Attack:{attack['attack']}" 
    
    def defense(self, battle_infos_defense):
        attack = PokemonAPI().get_infos_battle(battle_infos_defense)
        return f" Defense:{attack['defense']}"
    
    def special_attack(self, battle_infos_special_attack):
        attack = PokemonAPI().get_infos_battle(battle_infos_special_attack)
        return f" Special Attack:{attack['special-attack']}"

    def special_defense(self, battle_infos_special_defense):
        attack = PokemonAPI().get_infos_battle(battle_infos_special_defense)
        return f" Special Defense:{attack['special-defense']}"
        
    def speed(self, battle_infos_speed):
        attack = PokemonAPI().get_infos_battle(battle_infos_speed)
        return f" Speed:{attack['speed']}"
    #Aqui acaba as informações de batalha.
    
    def show_picture(self, picture):
        show_picture = PokemonAPI().get_main_pokemon(picture)
        return show_picture['sprites']['front_default']