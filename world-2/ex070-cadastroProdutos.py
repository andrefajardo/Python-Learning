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
title = ' CADASTRO DE PRODUTOS '

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
total = 0.0
count = 0
expensive = 0
########################################### Code #################################################

while True:
    productname = str(input('Informe o nome do produto: ').strip().capitalize())
    price = float(input('Informe o preço do produto (0,00): R$').strip().capitalize())
    total += price
    count += 1
    if count == 1:
        cheaperName = productname
        cheaperprice = price
    else:
        if cheaperprice > price:
            cheaperName = productname
            cheaperprice = price
    if price > 1000:
        expensive += 1
    option = ' '
    while option not in 'SN':
        option = str(input('Gostaria de continuar? [S/N]: \n').strip().upper()[0])
    if option == 'N':
        break

print('=+='*30)
print(f'O valor total de suas compras foi de R$ {total:.2f}.\n'
      f'Você comprou {expensive} produtos com valor acima de R$ 1000.00.\n'
      f'O produto mais barato adiquirido foi o {cheaperName}, no valor de R$ {cheaperprice:.2f}.')
print('=+='*30)

