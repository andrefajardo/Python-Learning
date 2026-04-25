################################ SECTION 0 - IMPORTS ###################################

import random
from time import sleep
from datetime import datetime

################################ SECTION 1- HEADER ######################################

frame = '==='
title = ' FATORIAL '

print( frame * 30)
print('===', ' ' * 84, '===', sep='')
print(f"=== {title:^82} ===")
print('===', ' ' * 84, '===', sep='')
print(frame * 30, '\n')

################################# SECTION 2 - FUNCTIONS ######################################

def msg(txt):
    length = len(txt)
    frame = length + 10
    print(f'#'*frame)
    print(f'{txt:^{frame}}')
    print(f'#'*frame)

def fatorial(n, show):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não o processo de cálculo.
    :return: O valor do fatorial de um número n.
    """

    f = 1
    if show == 'S':
        print(f"{cor['amarelo']}Calculando {n}! = ", end='')
        for c in range(n, 0, -1):
            f *= c
            if show:
                if c > 1:
                    print(f"{c} x ", end='')
                    sleep(0.3)
                else:
                    print(f"{c} = ", end='')
    if show == 'S':
        print(f"{cor['verde']}{f}{cor['limpa']}")
    if show == 'N':
        for c in range(n, 0, -1):
            f *= c
        print(f"O fatorial de {n} é {cor['verde']}{f}{cor['limpa']}")

################################ SECTION 3 - VARIABLES #####################################

cor = {'limpa': '\033[m',
       'vermelho': '\033[1:31m',
       'verde': '\033[1:32m',
       'amarelo': '\033[1:33m'}

################################# SECTION 4 - CODE #####################################

value = int(input("Informe um valor inteiro para o cálculo do fatorial: "))
option = str(input("Deseja ver o processo de cálculo? [S/N] ")).strip().upper()[0]
fatorial(value, option)
help(fatorial)

################################# SECTION 5 - ANOTHER WAY #####################################

def fatorial_recursivo(n):
    if n == 0:
        return 1
    else:
        return n * fatorial_recursivo(n - 1)