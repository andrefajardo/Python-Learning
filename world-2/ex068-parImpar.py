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
title = ' PAR OU IMPAR '

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
cont = 0
########################################### Code ##################################################

while True:
    option = str(input('Vamos jogar par ou impar. Faça sua escolha [PAR ou IMPAR]: ').strip().upper()[0])
    if option == 'PAR':
        compOption = 'IMPAR'
    else:
        compOption = 'PAR'

    print('\n',"*"*30)
    numb = int(input(' Agora informe seu número: ').strip())
    print('',"*"*30)
    compNumb = random.randint(0,11)

    sleep(2)
    if (compNumb + numb)%2 == 0:
        winner = 'P'
    else:
        winner = 'I'

    if winner == option:
        print(f' Eu escolhi {compNumb}. Você {colors['greenBold']}GANHOU{colors['clean']}!')
        cont += 1
    else:
        print(f' Eu escolhi {compNumb}. Você {colors['greenBold']}PERDEU{colors['clean']}!')
        print(f' Você terminou com {cont} vitória(s).')
        break
print('\n ---> G A M E    O V E R <---')