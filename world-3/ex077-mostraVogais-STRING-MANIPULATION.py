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
title = ' MOSTRA VOGAIS '

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
words =''
########################################### Code #################################################

while True:
    print('Informe as palavras para análise:\n')
    word = str(input('Informe o nome do produto: ').strip().upper())
    words += f'{word}-'
    option = ' '
    while option not in 'SN':
        option = str(input('Gostaria de continuar? [S/N]: \n').strip().upper()[0])
    if option == 'N':
        break

wordsLength = len(words)
words = words[:wordsLength - 1]  ### extracting the last "-" with "-1".
words2 = words.split('-')
words3 = tuple(words2)

print(' VOGAIS ENCONTRADAS '.center(90, '='))
for count in words3:
    print('\n', count, '--> ', end='')
    for letter in count:
        if letter in 'AEIOU':
            print(letter,' ', end='')
print('\n')
print(' FIM '.center(90, '='))
