##################################################################################################
###
###     Curso em Vídeo - Curso de Python - Mundo 3
###     Prof. Gustavo Guanabara
###
###     Module 3 Description: A set of exercises about data structure, functions, modules and package, error handling, etc.
###
###     student:  André Fajardo
###
##################################################################################################
####################################   Imported Modules  #########################################
from mailcap import findmatch

# Import exemples
# from datetime import datetime
# from itertools import count

from random import randint

######################################  Inicial Label  ###########################################
frame = '==='
title = ' SORTEIO DE NÚMEROS '

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

num1 = randint(0,9)
num2 = randint(0,9)
num3 = randint(0,9)
num4 = randint(0,9)
num5 = randint(0,9)

########################################### Code #################################################

numbers = (num1, num2, num3, num4, num5)

print(f'Os valores aleatórios são: {numbers}')
ordenedNumbers = sorted(numbers)
print(f'O menor valor é: {ordenedNumbers[0]}')
print(f'O maior valor é: {ordenedNumbers[4]}')



####################################### Alternative Way ##########################################

################################ SEÇÃO 0 ###################################
import random
################################ SEÇÃO 1 ###################################
msg = (' NÚMEROS ALEATÓRIOS ')
print('-=-' * 27)
print('{: ^80}'.format(msg))
print('-=-' * 27)
################################ SEÇÃO 3 ####################################
valor =(random.randint(0, 10), random.randint(0, 10), random.randint(0, 10),
        random.randint(0, 10), random.randint(0, 10))
menor = maior = valor[0]
c = 0
################################ SEÇÃO 4 ####################################
print(f'Os seguintes valores foram sorteados: {valor}')
while c in range(0, 5):
    if valor[c] > maior:
        maior = valor[c]
    elif valor[c] < menor:
        menor = valor[c]
    c += 1
print(f'\nO maior valor foi {maior} e o menor valor foi {menor}')
print(f'O maior valor foi {max(valor)} e o menor valor foi {min(valor)}')

