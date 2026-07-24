from utils import layout, validation, control, constants

# 1. Configurações Iniciais
layout.header(' APLICAÇÃO DE CADASTRO SIMPLES ')
opcoes = ["Listar Pessoas", "Cadastrar Pessoa", "Sair"]

# 2. Loop Principal Controlado
while True:
    layout.msg("MENU PRINCIPAL", opcoes)
    choise = validation.valid_option(1, len(opcoes))

    # Se a escolha for a última opção (Sair)
    if choise == 3:
        control.actions(3)  # Apenas exibe a mensagem de despedida
        break  # Sai do loop principal de forma limpa
    try:
        control.actions(choise)
    except Exception as error:
        print(f"{constants.colors['vermelho']}ERRO: {error}{constants.colors['limpa']}\n")
    else:
        print(f"{constants.colors['verde']}Operação concluída!{constants.colors['limpa']}\n")