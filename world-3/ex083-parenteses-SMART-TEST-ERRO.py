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
from operator import index

# Import exemples
# from datetime import datetime
# from itertools import count

######################################  Inicial Label  ###########################################
frame = '==='
title = ' VERIFICAR PARÊNTESES EM EXPRESSÕES '

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
openPar = []
closePar = []
status = 'Ok'
########################################### Code #################################################

express = str(input('Digite a expressão para análise usando números [0-9]\n,'
                    'operadores [+,-,*,/] e separadores "(" e ")": ').strip())

express.split()
for pos, value in enumerate(express):
    if value == '(':
        openPar.append(pos)
    if value == ')':
        closePar.append(pos)
    if len(closePar) > len(openPar):  # verify if a closing parenthesis appears before an opening one, digit by digit.
        status = 'Erro'
        break
if (len(openPar) == len(closePar)) and (status == 'Ok'):
    print(f'\nA expressão "{colors["greenBold"]}{express}{colors["clean"]}" está correta!.')
else:
    print(f'\nA expressão "{colors["redBold"]}{express}{colors["clean"]}" apresenta erros.')
