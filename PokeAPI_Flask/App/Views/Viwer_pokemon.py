"""
Aqui é a visualização do Projeto tudo oq vai ser jogado na tela é apresentado por aqui.
Pode conter outras coisas como um HTML, mas aqui é tudo oq o usuário vai ver.
"""
from App.Controllers.controller_pokemon import test_id_name

def request_id():
    req_id = input("id: ")
    print(f'O nome do seu Pokemon é o: {test_id_name(req_id)}')


def request_pokemon():
    req_name = input("Name of Pokemon: ")
    return req_name


request_id()