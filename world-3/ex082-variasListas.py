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
title = ' VARIAS LISTAS '

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
evenNums = []
oddNums = []
########################################### Code #################################################

print('Informe valores para a listagem: ')

while True:
    num = int(input('Digite um número [0-10]: ').strip())
    if num in numbers:
        print(f'O número {colors["redBold"]}{num}{colors["clean"]} já foi adicionado. Tente outro número.')
        continue
    else:
        numbers.append(num)
    count += 1
    option = str(input('Deseja continuar? [S/N]: ').strip().upper()[0])
    if option == 'N':
        break
print(f'Foram digitados ao todo {count} números.')

for pos, value in enumerate(numbers):
    if value % 2 == 0:
        evenNums.append(value)
    else:
        oddNums.append(value)

print(f'\nOs valores digitados foram {colors["greenBold"]}{numbers}{colors["clean"]}.')
print(f'\nOs valores pares foram {colors["blue"]}{evenNums}{colors["clean"]}.')
print(f'\nOs valores impares foram {colors["redBold"]}{oddNums}{colors["clean"]}.')
