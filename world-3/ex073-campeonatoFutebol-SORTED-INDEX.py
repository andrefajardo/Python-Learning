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
from mailcap import findmatch

# Import exemples
# from datetime import datetime
# from itertools import count

######################################  Inicial Label  ###########################################
frame = '==='
title = ' CAMPEONATO DE FUTEBOL '

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
brazilianChampionship = (
    "Flamengo",
    "Internacional",
    "Atlético-MG",
    "São Paulo",
    "Fluminense",
    "Grêmio",
    "Palmeiras",
    "Santos",
    "Athletico-PR",
    "Corinthians",
    "Bragantino",
    "Ceará",
    "Atlético-GO",
    "Bahia",
    "Sport",
    "Vasco",
    "Fortaleza",
    "Goiás",
    "Coritiba",
    "Botafogo"
)

pos = 0
########################################### Code #################################################

print(f'Os cinco primeiros colocados no "Brasileirão" são: ')
for pos in range(0,5):
    print(f'{pos + 1}° - {brazilianChampionship[pos]}')

print(f'\nOs quatro últimos colocados no "Brasileirão" são: ')
print(f'{brazilianChampionship[20:15:-1]}')  ### starting from the last one to 16°
print(f'{brazilianChampionship[-4:]}')       ### starting from the 16° to end

print(f'\nOs times que disputam o campeonato neste ano são: ')
print(f'{sorted(brazilianChampionship)}')

print(f'\nO Fluminense ocupa a {brazilianChampionship.index("Fluminense") + 1}ª posição na tabela de classificação.')
