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
from time import sleep
import random
######################################  Inicial Label  ###########################################
frame = '==='
title = ' PROGRESSÃO ARITIMÉTICA '

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

########################################### Code #################################################

sumValues = 0
c = 1

##################################################################################################

print('VAMOS EXIBIR OS PRIMEIROS 10 TERMOS DE UMA P.A. \n')

inicialNum = int(input('Informe o primeiro termo da P.A.: '))
step = int(input('Informe a razão da P.A.: '))

for c in range(1, 11):
    num = inicialNum + ( c -1 ) * step
    print(' {}° Termo - {}'.format(c, num))
print('\n===> ACABOU <===')

##################################### Alternative Code ##########################################

c = 1

print('==='*30)
print('VAMOS EXIBIR OS PRIMEIROS 10 TERMOS DE UMA P.A. \n')

inicialNum = int(input('Informe o primeiro termo da P.A.: '))
step = int(input('Informe a razão da P.A.: '))
option = 'S'
term = 11
while option != 'N':
    while c != term:
        num = inicialNum + (c - 1) * step
        print(' {}° Termo - {}'.format(c, num))
        c += 1
    print('\n===> ACABOU <===')
    option = str(input('Gostaria de continuar (S / N): ').strip().capitalize())
    if option == 'S':
        term = 11 + (int(input('Gostaria de ver quantos termos mais (n°): ')))

