##################################################################################################
###
###     Curso em Vídeo - Curso de Python - Mundo 3
###     Prof. Gustavo Guanabara
###
###     Module 3 Description: A set of exercises about data structure, functions, modules and
###     package, error handling, etc.
###
###     student:  André Fajardo
###
##################################################################################################
####################################   Imported Modules  #########################################

import datetime

######################################  Inicial Label  ###########################################
frame = '==='
title = ' CARTEIRA DE TRABALHO '

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
personData = dict()
nowadays = datetime.date.today()
########################################### Code #################################################

personData['name'] = str(input('Informe o seu nome: ').strip().lower())
personData['bornDate'] =  int(input('Informe o ano de nascimento: '))
personData['CTPS'] =  int(input('Informe o número da CT [0 - se não possuir]: ').strip().lower())
if personData['CTPS'] != 0:
    personData['contractYear'] = int(input('Informe o ano do último contrato: '))
    personData['salary'] = float(input('Informe o valor do último salário: R$'))
    personData['retired'] = 30 - (int(nowadays.year) - personData['contractYear'])
else:
    personData['retired'] = 30

print(f'Nome: {personData['name']}\n',
      f'Idade: {int(nowadays.year) - personData['bornDate']}\n',
      f'N° CTPS: {personData['CTPS']}\n')
if (personData['CTPS']) != 0:
  print(f'Ano de Contratação: {personData['contractYear']}\n',
        f'Salário: R${personData['salary']:.2f}\n',
        f'Anos para Aposentadoria: {personData['retired']}')


