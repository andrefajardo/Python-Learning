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
title = ' CLASSIFICAÇÃO POR GRUPOS '

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
birthDate = '00/00/0000'
adults = 0
notAdults = 0
########################################### Code #################################################

print('CLASSIFICAÇÃO DE PESSOAS POR FAIXA ETÁRIA \n')


for c in range(1, 8):
    birthDate = str(input('Informe a {}ª data de nascimento (dd/mm/yyyy): '.format(c)))
    birthDate = datetime.strptime(birthDate, "%d/%m/%Y").date()
    ## yearsOld = relativedelta(datetime.today(), birthDate)
    yearsOld = datetime.today().year - birthDate.year
    if yearsOld >= 18:
        adults += 1
    else:
        notAdults += 1
print('O grupo de adultos possui {} pessoas.'.format(adults))
print('O grupo de menores de idade possui {} pessoas.'.format(notAdults))



