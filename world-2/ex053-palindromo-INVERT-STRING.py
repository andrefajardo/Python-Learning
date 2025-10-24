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
title = ' DETECTOR DE PALÍNDROMO '

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

print('VAMOS VERIFCAR SE UMA PALAVRA É PALÍNDROMO \n')

word = str(input('Informe a palavra para análise: ').strip())
## We could also use this code
# words = word.split()
# joinWords = ''.join(words)
word = word.replace(' ','')
drow = word[::-1]   ### Use this command to invert a string

if word == drow:
    print('A paravra/frase "{}" {}é{} um PALÍNDROMO.'.format(word, colors['greenBold'], colors['clean']))
else:
    print('A paravra/frase "{}" {}NÃO{} é um PALÍNDROMO.'.format(word, colors['redBold'], colors['clean']))


