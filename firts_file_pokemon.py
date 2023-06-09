"""
Aqui fica os primeiros testes e linhas do primeiro arquivo antes do MVC.
"""
import requests

# Aqui temos todos os POKEMONS disponivies em nosso game.
def list_all_names():
    api = 'https://pokeapi.co/api/v2/pokemon/?limit=200'
    all_name = requests.get(api).json()
    pokemons = []
    for pokemon in all_name["results"]:
        pokemons.append(pokemon['name'])
    return pokemons

#Um unico pokemon api = 'https://pokeapi.co/api/v2/pokemon/squirtle'
#Quebrar o limite default do site de 20 pokemons -> ?limit=x -> https://pokeapi.co/api/v2/pokemon/?limit=50

# Aqui comeca com os tres primeiros POKEMONS disponiveis para serem escolhidos.
p_1 = 'https://pokeapi.co/api/v2/pokemon/squirtle'
p_2 = 'https://pokeapi.co/api/v2/pokemon/bulbasaur'
p_3 = 'https://pokeapi.co/api/v2/pokemon/charmander'
squirtle = requests.get(p_1).json()
bulbasaur = requests.get(p_2).json()
charmander = requests.get(p_3).json()


def first_poke():
    print(f"Escolha o seu primeiro pokemon!\n" + squirtle['name'].upper() + ' ' + bulbasaur['name'].upper() + ' ' +  charmander['name'].upper() + "\n")
    choice = input("\n Qual a sua escolha? Digite o nome do pokemon: ").lower()

    if choice == squirtle['name'].lower():
        pokemon = squirtle
    elif choice == bulbasaur['name'].lower():
        pokemon = bulbasaur
    elif choice == charmander['name'].lower():
        pokemon = charmander
    else:
        print("Pokemon inválido! Tente novamente.")
        return first_poke()

    print(f"Aqui temos as informações do seu pokemon: {pokemon['name'].upper()}")
    poke_abilities(pokemon)

def poke_info():
    pokemon = input("Você deseja as informações de qual POKEMON?\n")
    pokemons = list_all_names() # Aqui estamos pegando toda a resposta da funcao e passando ela para uma variavel.
    print('Aqui estão as informações do seu pokemon:\n')
    if pokemon in pokemons:
        pokemon_api = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'# Aqui colocamos a variavel no final da URL para realizar uma busca nas informacoes.
        pokemon_api_json = requests.get(pokemon_api).json()# como tudo se trata de formatos da WEB precisamos convertar todas as URLs para JSON.

       #Agora é necessário achar as evoluções do pokemon escolhido.
        specie_api = pokemon_api_json['species']['url']#Dentro da URL do POKEMON_API vai ter uma CHAVE especies e uma URL onde vao conter as caracteristicas dos pokemons.
        specie_api_json = requests.get(specie_api).json()# É necessário colocar tudo em .JSON
        evolution_api =  specie_api_json['evolution_chain']['url']# AQUI QUE A MAGICA ACONTECE PQP ISSO DEMOROU DEMAIS, as evolucoes estao nessa chave!!!!!!!!!!!PQPQ
        evolution_api_json = requests.get(evolution_api).json()# É necessário colocar tudo em .JSON
        #Agora a ideia aqui é pegar as evoluções e armazenar em algum lugar fora da URL.
        evolutions = []# tem que ser em lista pq tudo no python e lista
        essa_var_e_foda =evolution_api_json['chain']#Aqui vai ficar so os nomes das evolucoes
        while essa_var_e_foda:
            evolutions.append(essa_var_e_foda['species']['name'])#agora sao so os nomes das evolucoes na lista
            essa_var_e_foda = essa_var_e_foda['evolves_to'][0] if essa_var_e_foda['evolves_to'] else None #Aqui matamos o while como var = var toda vez que va[evolve][0] for diferente de None.
        #Informações do POKEMON.
        print(f"Name: {pokemon_api_json['name']}")
        print(f"Type(s): {[t['type']['name'] for t in pokemon_api_json['types']]}")
        print(f"Abilities: {[a['ability']['name'] for a in pokemon_api_json['abilities']]}")
        print(f"Weight: {pokemon_api_json['weight']}")
        print(f"As evoluções do seu pokemon são às: {' -> ' .join(evolutions)}") #Essa linha é uma brisa, ela concatena os elementos da lista com a seta ->
    else:
        print("Seu POKEMON não se ecnontra em nosso mundo POKEMON.\n Por favor verifique se ele está nessa lista e tente novamente.")
        print(list_all_names())


def poke_abilities(pokemon):
    print('Habilidades')
    for i in pokemon['abilities']:
        print(i['ability']['name'])

"""
def choce_your_poke():
    poke = input("Escolha um pokemon, para a sua batalha.")
    if poke in names():
        print("Vamos para batalha")
    else:
        print("Pokemon não encontrando.")
"""

def main():
    poke_info()


"""
api = 'https://pokeapi.co/api/v2/pokemon/squirtle'
    res=requests.get(api)
    teste=res.json()
    #pegar_habilidades(teste)
"""

#Estou criando uma nova linha s[o para um teste do GIT/ ]

#first_poke()
#print(list_all_names())
#print(choce_your_poke())
main()

if __name__ == '__main__':
    main()
