from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/pokemon/<pokemon_name>')
def get_pokemon_info(pokemon_name):
    # Faça uma solicitação à PokeAPI para obter informações sobre o Pokémon
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
    if response.status_code == 200:
        pokemon_data = response.json()
        # Processar os dados e retornar uma resposta
        return f'Informações sobre {pokemon_name}: {pokemon_data}'
    else:
        return f'Pokémon não encontrado: {pokemon_name}', 404


if __name__ == '__main__':
    app.run(debug=True)
