################################ SECTION 0 - IMPORTS ###################################
import random
from time import sleep
from pprint import pprint
from operator import itemgetter
from datetime import datetime
################################# SECTION 1 - FUNCTIONS ######################################

def sum_ode(values):
    sum_nums = 0
    ordered = sorted(values)
    msg(' Os valores sorteados foram ')
    print(ordered)
    for num in range(0, len(ordered)):
        if ordered[num] % 2 == 0:
            sum_nums += ordered[num]
    print(f'A soma dos valores pares é: {sum_nums}.\n')


def sorter():
    values = [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100),
             random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]
    return values



################################ SECTION 2- HEADER ######################################

frame = '==='
title = ' SORTEIA & SOMA '

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

values = sorter()
sum_ode(values)