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
from itertools import count
####################################   Imported Modules  #########################################
from time import sleep
import random
######################################  Inicial Label  ###########################################
frame = '==='
title = ' SOMA DE VALORES '

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

########################################### Code #################################################
sumValues = 0
count = 0

print('VAMOS EXIBIR UMA SOMA DOS PARES \n')

print('Informe 6 valores: \n')
for c in range(1, 7):
    num = int(input('Informe o {}° valor: '.format(c)).strip())
    if num % 2 == 0:
        sumValues += num
        count += 1

print('A soma dos {} valores pares informados é {}.'.format(count, sumValues))