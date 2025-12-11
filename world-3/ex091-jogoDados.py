##################################################################################################
###
###     Curso em Vídeo - Curso de Python - Mundo 3
###     Prof. Gustavo Guanabara
###
###     Module 3 Description: A set of exercises about data structure, functions, modules and
###     package, error handling, etc.
###
###     student:  André Fajardo
###
##################################################################################################
####################################   Imported Modules  #########################################
from operator import itemgetter
# Import exemples
# from datetime import datetime
# from itertools import count

from random import randint
from random import sample
from time import sleep

######################################  Inicial Label  ###########################################
frame = '==='
title = ' JOGO DE DADOS '

print( frame * 30)
print('===', ' ' * 84, '===', sep='')
print(f"=== {title:^82} ===")
print('===', ' ' * 84, '===', sep='')
print(frame * 30, '\n')

###################################   Colors Arguments   #########################################

### The code formatation ASCII is: \033["cod style";"cod text color";"cod background color"m
colors = {
    'backGreen':'\033[0;;42m',
    'greenBold':'\033[1;32m',
    'backYellow':'\033[0;;43m',
    'red':'\033[0;31m',
    'redBold':'\033[1;31m',
    'blue':'\033[0;34m',
    'inverted':'\033[7m',
    'clean':'\033[m'
}

########################################### Variables ############################################
rounds = dict()
########################################### Code #################################################

for count in range(1,5):
    rounds[f'player{count}:'] = randint(0, 6)

for k, v in rounds.items():
    print(f'{k}: {v}')
    sleep(0.5)

# ordenatedListRounds = sorted(rounds.items(), key=lambda x: x[1], reverse=True)
# another way to put in order
ordenatedListRounds = sorted(rounds.items(), key=itemgetter(1), reverse=True)
ordenatedRounds = dict(ordenatedListRounds)
print( frame * 30)
print(f'Jogadores que mais pontuaram:')
print( frame * 30)

for k, v in ordenatedRounds.items():
    print(f'{k}: {v}')
    sleep(0.5)

