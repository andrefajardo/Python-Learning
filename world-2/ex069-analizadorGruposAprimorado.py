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
birthDate = ''
name = ''
nameOlder = ''
gender = ''
averageAge = 0
older = 0
numberWoman = 0
adult = 0
totalMan = 0
total = 0
########################################### Code #################################################

print('ANALISADOR DE GRUPOS DE PESSOAS \n')


while True:
    name = str(input('Informe o nome da pessoa: ').strip().capitalize())
    birthDate = str(input('Informe a data de nascimento (dd/mm/yyyy): ').strip())
    birthDate = datetime.strptime(birthDate, "%d/%m/%Y").date()
    yearsOld = datetime.today().year -birthDate.year
    gender = ' '
    while gender not in 'MF':
        gender = str(input('Informe o sexo (M/F): ').strip().capitalize())
    averageAge += yearsOld
    total += 1
    if gender == 'M':
        totalMan += 1
    if (yearsOld > older) and (gender == 'M'):
        nameOlder = name
        older = yearsOld
    if (gender == 'F') and (yearsOld < 20):
        numberWoman += 1
    if yearsOld > 18:
        adult += 1
    option = str(input('Gostaria de continuar a cadastrar? [S/N]').strip().upper()[0])
    if option == 'N':
        break


print('\n===================================================================================\n')
print('A média de idade das pessoas é de {} anos.\n'
      'Existe {} adultos no grupo.\n'
      'O homem mais velho é o Sr.{}, que tem {} anos de idade.\n'
      'Foram cadastrados {} homens no sistema.\n'
      'No grupo temos {} mulheres com idade inferior a 20 anos.'.format(averageAge/total, adult, nameOlder, older, totalMan, numberWoman))
print('\n===================================================================================')