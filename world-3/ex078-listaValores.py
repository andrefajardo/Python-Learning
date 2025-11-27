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

# Import exemples
# from datetime import datetime
# from itertools import count

######################################  Inicial Label  ###########################################
frame = '==='
title = ' LISTA DE VALORES '

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
count = 0
numbers = []
listMax = []
listMin = []
########################################### Code #################################################

print('Informe cinco valores para análise: \n')
while count < 5:
    numbers.append(int(input('Digite um número: ')))
    count += 1

maxNum = max(numbers)
minNum = min(numbers)
for pos, value in enumerate(numbers):
    if value == minNum:
        listMin.append(pos)
    if value == maxNum:
        listMax.append(pos)
print(f'O menor valor da lista é {minNum}, na posição {listMin}.')
print(f'O maior valor da lista é {maxNum}, na posição {listMax}.')

