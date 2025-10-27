##################################################################################################
###
###     Curso em Vídeo - Curso de Python - Mundo 2
###     Prof. Gustavo Guanabara
###
###     Module 2 Description: A set of exercises about repetition and decision structures used
###     alone or nested.
###
###     student: André Fajardo
###
##################################################################################################

####################################   Imported Modules  #########################################
## Import Exemple ##
## from time import sleep
## import random
######################################  Inicial Label  ###########################################
frame = '==='
title = ' SEQUÊNCIA DE NÚMEROS DIGITADOS '

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

######################################## Variables ################################################

num = 0
count = 0
total = 0

########################################### Code ##################################################
while num != 999:
    num = int(input('Digite um número [999 Interrompe]: ').strip().upper())
    if num == 999:
        break
    else:
        count += 1
        total += num
print(f'O total de números digitados foi {count} e a soma dos valores é {total}.')
