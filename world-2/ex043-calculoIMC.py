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

#####################################  Inicial Label  ############################################
frame = '==='
title = ' CÁLCULO IMC '

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

###################################   Modules Imported   #########################################

import math

########################################### Code #################################################

weight = float(input('Informe o seu peso (kg): ').strip())
height = float(input('Informe a sua altura (cm): ').strip())

imc = weight / (height/100 * height/100)

if imc < 18.5 :
    print('Seu IMC é {}{:.2f}{}, portanto você está abaixo do peso.'.format(colors['red'], imc, colors['clean']))
elif (imc >= 18.5) and (imc < 25):
    print('Seu IMC é {}{:.2f}{}, portanto você está no peso ideal.'.format(colors['greenBold'], imc, colors['clean']))
elif (imc >= 25) and (imc < 30):
    print('Seu IMC é {}{:.2f}{}, portanto você está com sobrepeso.'.format(colors['backYellow'], imc, colors['clean']))
elif (imc >= 30) and (imc < 35):
    print('Seu IMC é {}{:.2f}{}, portanto você está com OBESIDADE.'.format(colors['red'], imc, colors['clean']))
else:
    print('Seu IMC é {}{:.2f}{}, portanto você está com OBESIDADE MÓRBIDA.'.format(colors['redBold'], imc, colors['clean']))


