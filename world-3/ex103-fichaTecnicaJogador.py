################################ SECTION 0 - IMPORTS ###################################

import random
from time import sleep
from datetime import datetime

################################ SECTION 1- HEADER ######################################

frame = '==='
title = ' FICHA TÉCNICA DO JOGADOR '

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


def card(player='', goals='0'):
    if player == '':
        player = '<DESCONHECIDO>'
    if goals == '':
        goals = '0'
    print(f'O jogador {player} fez {goals} gol(a) no campeonato.')

################################# SECTION 4 - CODE #####################################

player = str(input("Informe o nome do jogador: ")).strip().upper()
goals = str(input("Informe o número de gols marcados: "))
card(player, goals)
msg("teste")

############################# SECTION 5 - ANOTHER WAY ##################################