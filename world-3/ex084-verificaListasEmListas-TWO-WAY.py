##################################################################################################
###
###     Curso em Vídeo - Curso de Python - Mundo 3
###     Prof. Gustavo Guanabara
###
###     Module 3 Description: A set of exercises about data structure, functions, modules and package, error handling, etc.
###
###     student:  André Fajardo
###
##################################################################################################
####################################   Imported Modules  #########################################

# Import exemples
# from datetime import datetime
# from itertools import count

######################################  Inicial Label  ###########################################
frame = '==='
title = ' ANÁLISE DE LISTAS '

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
peopleList = []
people = []
numPeople = 0
havierPerson = []
lighterPerson = []
########################################### Code #################################################

while True:
    people.append(str(input('Informe o nome: ').strip().upper()))
    people.append(float(input('Informe o peso: ').strip()))
    peopleList.append(people[:])
    people.clear()
    numPeople += 1
    option = ' '
    while option not in 'SN':
        option = str(input('Gostaria de continuar? [S/N]: \n').strip().upper()[0])
    if option == 'N':
        break

havierPerson.append(peopleList[0][0])
havierWeight = float(peopleList[0][1])
lighterPerson.append(peopleList[0][0])
lighterWeight = float(peopleList[0][1])

for person in peopleList:
    if numPeople != 1:
        if float(person[1]) > float(havierWeight):
            havierWeight = float(person[1])
            havierPerson.clear()
            havierPerson.append(person[0])
        elif float(person[1]) == float(havierWeight):
            havierPerson.append(person[0])
        elif float(person[1]) < float(lighterWeight):
            lighterWeight = float(person[1])
            lighterPerson.clear()
            lighterPerson.append(person[0])
        elif float(person[1]) == float(lighterWeight):
            lighterPerson.append(person[0])
        else:
            continue

print(f'Ao todo, foram cadastradas {numPeople} pessoas.')
print(f'O maior peso foi de {havierWeight:.2f} kg. O peso de ', end='')
for w in havierPerson:
    print(f'{w}, ', end='' )
print(f'\nO menor peso foi de {lighterWeight:.2f} kg. O peso de ', end='')
for w in lighterPerson:
    print(f'{w}, ', end='' )


#==========================================Another Solution===========================================

################################ SEÇÃO 0 ###################################
#BIBLIOTECAS
################################ SEÇÃO 1 ###################################
msg = (' ANÁLISE DE LISTAS ')
print('-=-' * 27)
print('{: ^80}'.format(msg))
print('-=-' * 27)
cor = {'limpa': '\033[m',
       'vermelho': '\033[1:31m',
       'verde': '\033[1:32m',
       'amarelo': '\033[1:33m'}
################################ SEÇÃO 2 ####################################
cadastro = list()
gordo = list()
magro = list()
################################ SEÇÃO 3 ####################################
while True:
    cadastro.append([str(input('Informe o nome: ')), float(input('Informe o peso: '))])
    if len(cadastro) == 0:
        gordo = cadastro[:]
        magro = cadastro[:]
    status = str(input('Gostaria de inserir mais um cadastro? [S/N]: ').upper().strip())
    if status == 'N':
        break
for p in cadastro:
    if p[1] > gordo[0][1]:
        gordo.clear()
        gordo.append(p)
    elif p[1] == gordo[0][1]:
        gordo.append(p)
    elif p[1] < magro[0][1]:
        magro.clear()
        magro.append(p)
    elif p[1] == magro[0][1]:
        magro.append(p)
print('=+=' * 30)
print(f'Você inseriu {len(cadastro)} pessoa(s) no total.')
print(f'Destas, o menor peso era {magro[0][1]} de ', end='')
for m in magro:
    print(m[0], ' ', end='')
print(f'\nE o menor peso foi {gordo[0][1]} de ', end='')
for g in gordo:
    print(g[0], ' ', end='')
print('=+=' * 30)