from .. import constants

def valid_option(min_val=1, max_val=3):
    while True:
        try:
            # Capturamos o dado e limpamos espaços
            option = int(input(f"{constants.colors['amarelo']}  OPÇÃO: {constants.colors['limpa']}").strip())

            if min_val <= option <= max_val:
                return option  # Retorne apenas o NÚMERO

            print(f"{constants.colors['vermelho']}ERRO: Opção inválida!{constants.colors['limpa']}")
        except (ValueError, TypeError):
            print(f"{constants.colors['vermelho']}ERRO: Digite um número inteiro válido.{constants.colors['limpa']}")

# Verifica se o arquivo existe e é legível
def valid_arquive(arq_name):
    try:
        with open(arq_name, "r", encoding="utf-8") as arquivo:
            return True
    except FileNotFoundError:
        return False