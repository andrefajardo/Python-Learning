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
title = ' ESTATÍSTICA DE JOGO PLUS'

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
statisticBook = list()
playerStatistic = dict()
goals = list()
total = 0
num = 1
########################################### Code #################################################

while True:
    playerStatistic['Name'] = str(input(f'Nome do jogador: ').strip().lower())
    playerStatistic['Matches'] = int(input(f'Número de jogos: '))
    for count in range(1, playerStatistic['Matches'] + 1):
        goals.append(int(input(f'Gols marcados no {count}° jogo: ')))
    playerStatistic['Goals'] = goals.copy()
    goals.clear()
    statisticBook.append(playerStatistic.copy())
    option =' '
    if option not in 'S/N':
        option = str(input(f'Gostaria de inserir mais um jogador? [S/N]: ').strip().upper())
        if option == 'N':
            break

for playerStatistic in statisticBook:
    for goals in range(0, len(playerStatistic['Goals'])):
        total += playerStatistic['Goals'][goals]
    print('#'*80)
    print(f'[{num}] - O jogador {playerStatistic['Name']} marcou {total} gols.')
    total = 0
    num += 1
num = 0

while True:
    details = str(input(f'Informe o Nº do jogador para detalhar [N] para sair: ').strip().upper())
    if details == 'N':
        break
    else:
        if int(details) > len(statisticBook):
            print('Digite um valor válido.')
        else:
            print(f'#'*50)
            print(f'\n[{details}] - Nome: {statisticBook[int(details)-1]['Name']} - Partidas: {statisticBook[int(details)-1]['Matches']} - Gols: {statisticBook[int(details)-1]['Goals']}.\n')
            print(f'#'*50)