from .. import layout
from .. import validation
from .. import constants

def list_people():
    arquivo = "arquivo.txt"
    if validation.valid_arquive(arquivo):
        with open(arquivo, "r", encoding="utf-8") as file:
            people = file.readlines()
            if people:
                layout.sub_header("PESSOAS CADASTRADAS")
                for person in people:
                    print(person.strip())
            else:
                print(f"{constants.colors['amarelo']}Nenhuma pessoa cadastrada.{constants.colors['limpa']}")
    else:
        print(f"{constants.colors['vermelho']}ERRO: Arquivo não encontrado!{constants.colors['limpa']}")
