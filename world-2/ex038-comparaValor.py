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

import math
from time import sleep

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

print('Informe 2 números inteiros: ')
num1 = int(input('Primeiro número: ').strip())
num2 = int(input('Segundo número: ').strip())

if num1 == num2:
    print('Os números informados são iguais.')
elif num1 > num2:
    print('O primeiro número é maior.')
else:
    print('O segundo número é maior.')