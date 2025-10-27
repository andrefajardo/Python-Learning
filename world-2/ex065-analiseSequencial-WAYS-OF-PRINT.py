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
from time import sleep
import random
######################################  Inicial Label  ###########################################
frame = '==='
title = ' ANÁLISE DE SEQUÊNCIA '

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

option = 'S'
sumNumbers = 0
countNum = 0
num = 0


########################################### Code ##################################################

print('ANÁLISE DETALHADA DE VALORES DIGITADOS \n')

print('==='*30)

while option != 'N':
    if countNum == 0:
        num = int(input('Digite um número inteiro: ').strip())
        greaterNUm = num
        smallerNum = num
    else:
        num = int(input('Digite um número inteiro: ').strip().capitalize())
        if greaterNUm < num:
            greaterNUm = num
        elif smallerNum > num:
            smallerNum = num
    sumNumbers += num
    countNum += 1
    option = str(input('Gostaria de continuar? (S/N) : ').strip().capitalize())
    sleep(0.5)

################ More archaic form to print (%S) strings (%d) digits - Python 2 #################
averageValue = sumNumbers/countNum
print('\n===> ACABOU <===\n'
      '\nA média dos valores digitados é {%.2f}.\nOs menores e maiores valores digitados foram {%d} e {%d}.'%(averageValue, smallerNum, greaterNUm))

################ More improved way to print #################
print('\n===> ACABOU <===\n'
      '\nA média dos valores digitados é {}{:.2f}{}.\nOs menores e maiores valores digitados foram {}{} e {}{}.'.format(colors['redBold'], sumNumbers/countNum, colors['clean'], colors['redBold'], smallerNum, greaterNUm, colors['clean']))

################ Latest form to print #################
print('\n===> ACABOU <===\n'
      f'\nA média dos valores digitados é {colors['redBold']}{sumNumbers/countNum:.2f}{colors['clean']}.\nOs menores e maiores valores digitados foram {colors['redBold']}{smallerNum} e {greaterNUm}{colors['clean']}.')
