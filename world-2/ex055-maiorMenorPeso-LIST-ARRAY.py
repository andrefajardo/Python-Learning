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
title = ' MAIOR E MENOR PESOS '

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
weightList = []


########################################### Code #################################################

print('INFORMAÇÃO SOBRE PESOS \n')


for c in range(0, 5):
    weight = int(input('Informe o {}° peso (kg): '.format(c + 1)))
    weightList.append(weight)

weightList.sort()
print('O indivíduo mais pesado tem {} kg.'.format(weightList[4]))
print('O indivíduo mais leve tem {} kg.'.format(weightList[0]))

###################################### Alternative Code ##########################################

print('INFORMAÇÃO SOBRE PESOS \n')

for c in range(0, 5):
    weight = int(input('Informe o {}° peso (kg): '.format(c + 1)))
    if c == 0:
        heavier = weight
        lighter = weight
    else:
        if weight >= heavier:
            heavier = weight
        if weight <= lighter:
            lighter = weight

print('O indivíduo mais pesado tem {} kg.'.format(heavier))
print('O indivíduo mais leve tem {} kg.'.format(lighter))