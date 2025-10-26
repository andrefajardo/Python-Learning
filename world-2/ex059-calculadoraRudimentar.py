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
####################################   Imported Modules  #########################################

from datetime import datetime
from dateutil.relativedelta import relativedelta
from time import sleep
import random
from xmlrpc.client import DateTime

######################################  Inicial Label  ###########################################
frame = '==='
title = ' CALCULADORA RUDIMENTAR '

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
num1 = 0
num2 = 0
option = 99
result = 0
########################################### Code #################################################

print('*** OPERAÇÃO COM DOIS VALORES ***\n')
print('=+='*20)
while option != 5:
    num1 = int(input('Informe o primeiro valor: ').strip())
    num2 = int(input('Informe o segundo valor: ').strip())
    print('***'*30)
    option = int(input('Escolha a operação: \n'
                       '[ 1 ] - Soma\n'
                       '[ 2 ] - Subtração\n'
                       '[ 3 ] - Multiplicação\n'
                       '[ 4 ] - Divisão\n'
                       '[ 5 } - Sair\n'
                       'Opção: '))
    if option == 1:
        result = num1 + num2
        print('Resultado = {}'.format(result))

    elif option == 2:
        result = num1 - num2
        print('Resultado = {}'.format(result))
    elif option == 3:
        result = num1 * num2
        print('Resultado = {}'.format(result))
    elif option == 4:
        if num2 == 0:
            print('Erro: divisão por zero (0).')
        else:
            result = num1 / num2
            print('Resultado = {}'.format(result))
    elif option == 5:
        print('Obrigado por usar nosso sistema.')
    else:
        print('Opção inválida. Tente novamente.')
