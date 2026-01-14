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
title = ' ÁREA DO RETÂNGULO '

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
width = 0
length = 0
########################################### Code #################################################

def area(w, l):
    value = w * l
    print('')
    print('#'*30)
    print(f'A área do terreno é de: {value} m².')
    print('#' * 30, '\n')
    

width = float(input(f'Informe a largura do terreno: ').strip())
length = float(input(f'Informe o comprimento do terreno: ').strip())
area(width, length)
