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
title = ' LISTA INICIAL ORDENADA '

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
numbers = list()
listMax = list()
listMin = list()
########################################### Code #################################################

print('Informe cinco valores para análise: ')
while count < 5:
    num = int(input('Digite um número [0-10]: ').strip())
    if num in numbers:
        print(f'O número {colors["redBold"]}{num}{colors["clean"]} já foi adicionado. Tente outro número.')
        continue
    if count == 0:
        numbers.append(num)
        count += 1
        continue
    else:
        for pos, value in enumerate(numbers):
            if num < value:
                numbers.insert(pos, num)
                break
        else:
            numbers.append(num)
        count += 1
print('Os valores digitados em ordem crescente são: ', end='')
for value in numbers:
    print(f'{colors["blue"]}{value}{colors["clean"]}', end=' ')
