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
title = ' ANÁLISE DE GRUPO '

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
personGroup = dict()
personsList = list()
womenList = list()
totalpeople = 0
totalAge = 0
########################################### Code #################################################

while True:
    personGroup['Name'] = str(input('Informe o nome: ').strip().lower())
    personGroup['Age'] = int(input('Informe a idade: ').strip().lower())
    totalAge += personGroup['Age']
    personGroup['Gender'] = str(input('Informe o sexo [M/F]: ').strip().upper())
    while personGroup['Gender'] not in 'MF':
        personGroup['Gender'] = str(input('Por favor, informe o sexo? [M/F]: ').strip().upper())
    totalpeople += 1
    personsList.append(personGroup.copy())
    option = str(input('Gostaria de continuar? [S/N]: ').strip().upper())
    while option not in 'SN':
        option = str(input('Por favor, informe se gostaria de continuar? [S/N]: ').strip().upper())
    if option == 'N':
        break
print('#'*50)
print(f'O grupo possui {totalpeople} pessoas.\n'
      f'A média de idade é de {totalAge/totalpeople:5.2f}.')

for k in personsList:
    if k.get('Gender') == 'F':
        womenList.append(k.get('Name'))
print(f'As mulheres cadastradas foram: {womenList}')

print('*' * 80)
print('Lista de pessoas com idade acima da média:\n')
for k in personsList:
    if k.get('Age') > (totalAge/totalpeople):
        print(f'Nome = {k.get("Name")}; Idade = {k.get("Age")}')

