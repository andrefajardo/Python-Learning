from .. import layout
from .. import validation
from .. import constants

def register_person():
    arquivo = "arquivo.txt"
    layout.sub_header("CADASTRO DE PESSOA")

    while True:
        name = input(f"{constants.colors['amarelo']}NOME: {constants.colors['limpa']}").strip()
        age = input(f"{constants.colors['amarelo']}IDADE: {constants.colors['limpa']}").strip()

        if not name or not age:
            print(f"{constants.colors['vermelho']}ERRO: Nome e idade são obrigatórios!{constants.colors['limpa']}")
            return

        if not age.isdigit():
            print(f"{constants.colors['vermelho']}ERRO: Idade deve ser um número inteiro!{constants.colors['limpa']}")
            return

        with open(arquivo, "a", encoding="utf-8") as file:
            file.write(f"{name} - {age} anos\n")

        print(f"{constants.colors['verde']}Pessoa cadastrada com sucesso!{constants.colors['limpa']}")
        option = input(f"{constants.colors['amarelo']}Deseja cadastrar outra pessoa? (s/n): {constants.colors['limpa']}").strip().upper()
        if option == "N":
            break