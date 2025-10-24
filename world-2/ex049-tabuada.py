###################################################################################################
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

###################################   Imported Modules  #########################################
from time import sleep
import random
#####################################  Inicial Label  ############################################
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

print('VAMOS EXIBIR UMA TABUADA \n')

value = int(input('Informe o valor (0-10) para exibição da tabuada: ').strip())
for c in range(0, 10):
    result = c * value
    print(' {} x {} = {}'.format(c, value, result))

