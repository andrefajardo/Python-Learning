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
title = ' ANÁLISE DE TRIÂNGULOS '

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

colors = {
    'BackGren':'\033[0;;42m',
    'BackYellow':'\033[0;;43m',
    'red':'\033[0;31m',
    'redBold':'\033[1;31m',
    'greenBold':'\033[1;32m',
    'blue':'\033[0;34m',
    'inverted':'\033[7m',
    'clean':'\033[m'
}
side1 = float(input('Informe o primeiro lado do triângulo: ').strip())
side2 = float(input('Informe o segundo lado do triângulo: ').strip())
side3 = float(input('Informe o terceiro lado do triângulo: ').strip())

setSides = [side1, side2, side3]
setSides.sort()

if (setSides[0] + setSides[1]) < setSides[2]:
    print('As medidas informadas {}NÃO FORMAM{} um triângulo.'.format(colors['redB'], colors['clean']))
else:
    print('As medidas informadas {}FORMAM{} um triângulo.'.format(colors['inverted'], colors['clean']))
    if (side1 == side2) and (side2 == side3):
    ## you also use this
    ## if (side1 == side2 == side3):
    ##     --- code --- EQUILÁTERO
    ## elif (side1 != side2 != side3):
    ##     --- code --- ESCALENO
    ## else:
    ##     --- code --- ISÓSCELES
        print('O triângulo formado é {}EQUILÁTERO{}.'.format(colors['greenBold'], colors['greenBold']))
    elif (side1 == side2) or (side2 == side3) or (side1 == side3):
        print('O triângulo formado é {}ISÓSCELES{}.'.format(colors['greenBold'], colors['greenBold']))
    else:
        print('O triângulo formado é {}ESCALENO{}.'.format(colors['greenBold'], colors['greenBold']))



