################################ SECTION 0 - IMPORTS ###################################
import random
from time import sleep
from pprint import pprint
from operator import itemgetter
from datetime import datetime
################################# SECTION 1 - FUNCTIONS ######################################

def bigger(* values):
    ordered = sorted(values)
    maxvalue = ordered[-1]
    msg(' Os valores digitados foram ')
    print(values)
    sleep(0.3)
    print(f'O maior valor é: {maxvalue}.\n')


def escreva(msg):
    print('=' * (len(msg) + 4))
    print(f'  {msg}')
    print('=' * (len(msg) + 4))
    print()


################################ SECTION 2- HEADER ######################################

frame = '==='
title = ' ORDENANDO VALORES '

print( frame * 30)
print('===', ' ' * 84, '===', sep='')
print(f"=== {title:^82} ===")
print('===', ' ' * 84, '===', sep='')
print(frame * 30, '\n')
def msg(txt):
    length = len(txt)
    frame = length + 10
    print(f'#'*frame)
    print(f'{txt:^{frame}}')
    print(f'#'*frame)
################################ SECTION 3 - VARIABLES #####################################
cor = {'limpa': '\033[m',
       'vermelho': '\033[1:31m',
       'verde': '\033[1:32m',
       'amarelo': '\033[1:33m'}
################################# SECTION 4 - CODE #####################################

bigger(1, 2, 4, 3, 8, 5)
bigger(1,9,4)
bigger(8,7,2,4,1)