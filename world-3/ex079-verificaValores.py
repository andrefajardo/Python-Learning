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
title = ' VERIFICA LISTA DE VALORES '

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
count = 0
numbers = []
listMax = []
listMin = []
########################################### Code #################################################

print('Informe valores para a análise')
while True:
    num = (int(input('Digite um número inteiro [0-10]: ')))
    if num in numbers:
        print(f'O número {colors["redBold"]}{num}{colors["clean"]} já foi adicionado. Tente outro número.')
        continue
    else:
        numbers.append(num)
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        while resp not in 'SN':
            resp = str(input('Opção inválida! Quer continuar? [S/N]: ').strip().upper()[0])
        if resp == 'N':
            break
print(f'Os valores digitados foram: numbers {colors['blue']}{sorted(numbers)}{colors['clean']}')