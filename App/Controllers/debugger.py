"""
A ideia dessa arquivo é somente chamar as funções para ficar mais fácil com a tela splitada.
"""
import pprint
import controller_pokemon
import requests

pokemon = 'pikachu'
"""
#Show name
print(controller_pokemon.Pokemon().name(pokemon))
#Show_id
print(controller_pokemon.Pokemon().id(pokemon))
#get_weight
print(controller_pokemon.Pokemon().weight(pokemon))
#Type
print(controller_pokemon.Pokemon().types(pokemon))
#Evolves
print(controller_pokemon.Pokemon().evolutions(pokemon))
#abilities 
print(controller_pokemon.Pokemon().abilities(pokemon))
#Picture
print(controller_pokemon.Pokemon().show_picture(pokemon))

#Infos for battles
    #HP
print(controller_pokemon.Pokemon().HP(pokemon))
    #Attack
print(controller_pokemon.Pokemon().attack(pokemon))
    #Defense
print(controller_pokemon.Pokemon().defense(pokemon))
    #Special_Attack
print(controller_pokemon.Pokemon().special_attack(pokemon))
    #Special_Defense
print(controller_pokemon.Pokemon().special_defense(pokemon))
    #Speed
print(controller_pokemon.Pokemon().speed(pokemon))
"""
#print(controller_pokemon.Pokemon().abilities(pokemon))
test_index = controller_pokemon.PokemonAPI().get_main_pokemon(pokemon)
show_abilities = test_index["abilities"]
print(show_abilities)
show_name = show_abilities[0]["ability"]["name"]
print(show_name)
show_url = show_abilities[0]["ability"]["url"]
response = requests.get(show_url).json()
#print(response)
effect_url = response["effect_entries"]
effect = effect_url[1]["short_effect"]
pprint.pprint(effect)


"""
def info_battle(battle):
    main_url = controller_pokemon.PokemonAPI().get_pokemon(battle)
    for stat in main_url['stats']:
        print(stat)

info_battle(pokemon)

print(controller_pokemon.PokemonAPI().infos_battle(pokemon))
"""