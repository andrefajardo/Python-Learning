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
from itertools import count

from dateutil.relativedelta import relativedelta
from time import sleep
import random
from xmlrpc.client import DateTime

######################################  Inicial Label  ###########################################
frame = '==='
title = ' CAIXA ELETRÔNICO '

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
bills1 = bills10 = bills20 = bills50 = 0
########################################### Code #################################################

while True:
    cashValue = float(input('Informe o valor que deseja sacar: R$ '))

    if cashValue >= 50:
        bills50 = cashValue // 50
        cashValue = cashValue % 50
    if cashValue >= 20:
        bills20 = cashValue // 20
        cashValue = cashValue % 20
    if cashValue >= 10:
        bills10 = cashValue // 10
        cashValue = cashValue % 10
    if cashValue < 10:
        bills1 = cashValue

    print(f'Notas de R$ 50,00: {bills50:.2f}\n'
          f'Notas de R$ 20,00: {bills20:.2f}\n'
          f'Notas de R$ 10,00: {bills10:.2f}\n'
          f'Notas de R$  1,00: {bills1:.2f}\n')
    bills1 = bills10 = bills20 = bills50 = 0
    option = str(input('Gostaria de continuar sacando? [S/N]: ').strip().upper()[0])
    if option == 'N':
        break

print("=+="*30)
print(f"{'Obrigado por usar nossos serviços.':^80}")
print("=+="*30)