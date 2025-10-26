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
title = ' VERIFICA SEXO '

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
gender = 'I'
########################################### Code #################################################

print('VERIFICA SEXO \n')

gender = str(input('Informe o sexo (M/F): ').strip().upper()[0])
while (gender != 'M') and (gender != 'F'):
    print('Dados inválidos. Digite o sexo novamente.\n')
    gender = str(input('Informe o sexo (M/F): ').strip().upper()[0])



if gender == 'M':
    print('\n===================================================================================')
    print('\nA pessoa é do sexo MASCULINO.')
    print('\n===================================================================================')
else:
    print('\n===================================================================================')
    print('\nA pessoa é do sexo FEMININO.')
    print('\n===================================================================================')
