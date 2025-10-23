###################################################################################################
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

###################################   Imported Modules  #########################################
from time import sleep
import random
#####################################  Inicial Label  ############################################
frame = '==='
title = ' PEDRA - PAPEL - TESOURA '

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
print('Vou fazer minha escolha...')
jokenpoList = ['Pedra', 'Papel', 'Tesoura']
#computerOption = random.randint(1,3)
computerOption = random.choice(jokenpoList)
sleep(2)
humanOption = int(input('Faça a sua escolha: \n'
                   '1 - Pedra; \n'
                   '2 - Papel; \n'
                   '3 - Tesoura. \n'
                   'Opção: ').strip())
if humanOption == 1:
    humanOption = 'Pedra'
elif humanOption == 2:
    humanOption = 'Papel'
else:
    humanOption = 'Tesoura'

print('********************************************************************************')
if computerOption == humanOption:
    print('*** Empatamos. ***')
elif (computerOption == 'Pedra') and (humanOption == 'Tesoura') or (computerOption == 'Papel') and (humanOption == 'Pedra') or (computerOption == 'Tesoura') and (humanOption == 'Papel'):
    print('Escolhi {}{}{} e você {}{}{} \n*** VOCê PERDEU *** '.format(colors['greenBold'], computerOption, colors['clean'], colors['redBold'], humanOption, colors['clean']))
else:
    print('Escolhi {}{}{} e você {}{}{} \n*** VOCÊ GANHOU *** '.format(colors['redBold'], computerOption, colors['clean'], colors['greenBold'], humanOption, colors['clean']))
print('********************************************************************************')
