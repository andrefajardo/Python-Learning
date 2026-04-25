################################ SECTION 0 - IMPORTS ###################################

from time import sleep

################################ SECTION 1- HEADER ######################################

frame = '==='
title = ' HELP SYSTEM '

print( frame * 30)
print('===', ' ' * 84, '===', sep='')
print(f"=== {title:^82} ===")
print('===', ' ' * 84, '===', sep='')
print(frame * 30, '\n')

################################ SECTION 2 - VARIABLES #####################################

cor = {'limpa': '\033[m',
       'vermelho': '\033[1:31m',
       'verde': '\033[1:32m',
       'amarelo': '\033[1:33m'}

option = ''

################################# SECTION 3 - FUNCTIONS ######################################

def msg(txt):
    length = len(txt)
    frame = length + 10
    print(f'{cor["verde"]}#'*frame)
    print(f'{txt:^{frame}}')
    print(f'#'*frame, f'{cor["limpa"]}')

def helpSystem():
    """ -> Função para exibir o sistema de ajuda interativo. """
    msg('*** Help System ***')
    while True:
        option = str(input(f'{cor["vermelho"]}> Informe a função para ajuda ou "FIM" para sair: {cor["amarelo"]}'))
        if option.upper().strip() == 'FIM':
            break
        print(f'{cor['verde']}')
        help(option)
        print(f'{cor["limpa"]}')



################################# SECTION 4 - CODE #####################################

helpSystem()

############################# SECTION 5 - ANOTHER WAY ##################################

from time import sleep

c = ('\033[m',         # 0 - sem cores
     '\033[0;30;41m',  # 1 - vermelho
     '\033[0;30;42m',  # 2 - verde
     '\033[0;30;43m',  # 3 - amarelo
     '\033[0;30;44m',  # 4 - azul
     '\033[0;30;45m',  # 5 - roxo
     '\033[7;30m')     # 6 - branco

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}  ')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)

# Programa Principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)
