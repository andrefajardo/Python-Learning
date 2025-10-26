##################################################################################################
###
###     Curso em Vídeo - Curso de Python - Mundo 2
###     Prof. Gustavo Guanabara
###
###     Module 2 Description: A set of exercises about repetition and decision structures used
###     alone or nested.
###
###     student:  André Fajardo
###
##################################################################################################
####################################   Imported Modules  #########################################

from datetime import datetime
from dateutil.relativedelta import relativedelta
from time import sleep
import random
from xmlrpc.client import DateTime

######################################  Inicial Label  ###########################################
frame = '==='
title = ' ADIVINHAR O NÚMERO '

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
attempts = 1
########################################### Code #################################################

import random
from time import sleep
print('Vou pensar em um número de 0 a 5 e você deve tentar adivinhar qual é o número.\n')
numSort = random.randint(1, 3)
print('=+='*20)
print("PENSANDO...")
print('=+='*20)
sleep(3)
num = int(input('\nEscolha um número de 1 a 3: ').strip())
while numSort != num:
    print('Que pena! Você errou. Vamos tentar novamente'.format(numSort))
    num = int(input('Escolha outro número de 1 a 3: ').strip())
    attempts += 1
print('Parabéns, você acertou o número --> ({}) <-- na {}ª tentativa.'.format(num, attempts))
