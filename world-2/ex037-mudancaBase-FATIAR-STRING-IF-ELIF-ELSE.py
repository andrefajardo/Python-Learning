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

num = int(input('Informe um número inteiro para a mudança de base: ').strip())
option = int(input('Para qual base deseja converter:\n'
                   '1 - Binária;\n'
                   '2 - Octal;\n'
                   '3 - Hexadecimal.\n'
                   'Opção: '))

if option == 1:
    print('Na base binária o número {}{}{} decimal equivale a {}{}{}'.format(colors['greenBold'],num,colors['clean'], colors['greenBold'], bin(num)[2:], colors['clean']))
elif option == 2:
    print('Na base octal o número {}{}{} decimal equivale a {}{}{}'.format(colors['greenBold'], num, colors['clean'], colors['greenBold'], oct(num)[2:], colors['clean']))
elif option == 3:
    print('Na base hexadecimal o número {}{}{} decimal equivale a {}{}{}'.format(colors['greenBold'], num, colors['clean'], colors['greenBold'], hex(num)[2:], colors['clean']))
else:
    print('Opção inválida. Tente novamente.')
