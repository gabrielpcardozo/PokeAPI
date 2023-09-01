import sys
sys.path.insert(0, '/home/gcardozo/Projects/Python/PokeAPI/App/Controllers')

from App.Controllers import controller_pokemon

pokemon = 'pikcahu'
print(controller_pokemon.PokemonAPI().get_main_pokemon(pokemon))