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
title = ' ESTATÍSTICA DE JOGO '

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
playerStatistic = dict()
goals = list()
total = 0
########################################### Code #################################################

playerStatistic['Name'] = str(input(f'Nome do jogador: ').strip().lower())
playerStatistic['Matches'] = int(input(f'Número de jogos: '))
for count in range(1, playerStatistic['Matches'] + 1):
    goals.append(int(input(f'Gols marcados no {count}° jogo: ')))
    total += goals[count - 1]
playerStatistic['Goals'] = goals
print(playerStatistic)
print(f'O jogador {playerStatistic['Name']} marcou {total}')
for count in range(1,  playerStatistic['Matches'] + 1):
    print(f'O jogador {playerStatistic['Name']} marcou {playerStatistic['Goals'][count -1]} na {count}ª partida.')
