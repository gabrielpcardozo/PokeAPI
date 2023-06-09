"""
Aqui é a visualização do Projeto tudo oq vai ser jogado na tela é apresentado por aqui.
Pode conter outras coisas como um HTML, mas aqui é tudo oq o usuário vai ver.
"""
import controller_pokemon

def request_id():
    req_id = input("id: ")
    return req_id


def request_pokemon():
    req_name = input("Name of Pokemon: ")
    return req_name


controller_pokemon.take_pokemon_name(request_id())