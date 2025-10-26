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
from time import sleep
import random
######################################  Inicial Label  ###########################################
frame = '==='
title = ' SEQUÊNCIA DE FIBONACCI '

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

c = 1
term1 = 0
term2 = 1
nextNum = 0

##################################################################################################

print('VAMOS EXIBIR OS PRIMEIROS DA SEQUÊNCIA DE FIBONACCI \n')

termsAmount = int(input('Informe o número de termos de Fibonacci: ').strip())

print('==='*30)
print(term1,'-->',term2, end=' ')

while c != termsAmount - 1:
    nextNum = (term1) + (term2)
    print('-->', nextNum, end=' ')
    term1 = term2
    term2 = nextNum
    c += 1

print('\n===> ACABOU <===')
