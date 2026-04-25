################################ SECTION 0 - IMPORTS ###################################

import random
from time import sleep
from datetime import datetime

################################ SECTION 1- HEADER ######################################

frame = '==='
title = ' ANALISA INTEIRO '

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

################################# SECTION 3 - FUNCTIONS ######################################

def msg(txt):
    length = len(txt)
    frame = length + 10
    print(f'#'*frame)
    print(f'{txt:^{frame}}')
    print(f'#'*frame)

def newInput():
    """
    -> Solicita ao usuário que digite um número entre 1 e 100000.
    """
    while True:
        try:
            n = int(input('Digite um número entre 1 e 100000: '))
            if 1 <= n <= 100000:
                n = f'{cor["verde"]}Você digitou o número: {n}.{cor["limpa"]}'
                return n
        except ValueError:
            n = f'{cor["vermelho"]}Digite um número válido!{cor["limpa"]}'
            return n

################################# SECTION 4 - CODE #####################################

result = newInput()
print(result)

############################# SECTION 5 - ANOTHER WAY ##################################

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')