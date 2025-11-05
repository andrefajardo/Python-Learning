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
title = ' ANÁLISE DE VALORES '

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

########################################### Code #################################################

print('Informe quatro valores para análise: \n')
num1 = int(input('Informe o primeiro número inteiro: '))
num2 = int(input('Informe o segundo número inteiro: '))
num3 = int(input('Informe o terceiro número inteiro: '))
num4 = int(input('Informe o quarto número inteiro: '))
numbers = (num1, num2, num3, num4)

nine = numbers.count(9)
print(f'O número "9" apareceu {nine} vezes no grupo.')

try:
    three = numbers.index(3)
    print(f'O primeiro valor "3" está na posição {three + 1}.')
except ValueError:
    print(f'O valor "3" não está presente no grupo.')

countEven = 0
for c in range(0,4):
    if numbers[c]%2==0:
        countEven += 1
print(f'Foram digitados {countEven} números pares.')