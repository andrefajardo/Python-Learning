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

print('VAMOS EXIBIR A SOMA DE VALORES MULTIPLOS DE 3 NO INTERVALO DE 1 - 500\n')
sleep(2)
sum3 = 0
count = 0

for c in range(3, 501, 3):
    if c % 2 != 0:
        sum3 += c
        count += 1
        print(c,'', end='')
print('\n\nA soma dos {} números múltiplos de 3 no intervalo de 1 a 500 é {}.'.format(count, sum3))