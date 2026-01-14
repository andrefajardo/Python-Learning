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

import datetime
from time import sleep

######################################  Inicial Label  ###########################################
frame = '==='
title = ' AJUSTE DE MENSAGEM '

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

def msg(txt):
    length = len(txt)
    frame = length + 10
    print(f'#'*frame)
    print(f'{txt:^{frame}}')
    print(f'#'*frame)

def counter(start, finish, step):
    if ((finish < start) and (step > 0)):
        step = - step
    for value in range(start, finish, step):
        print(f'{colors['greenBold']}{value}{colors['clean']} ', end='')
        sleep(0.3)
    print('--> FIM!')
msg('CONTAGEM:  1 a 10')
counter(1, 11, 1)
print('\n')
msg('CONTAGEM:  10 a 0 PASSO 2')
counter(10, -1, -2)
print('')
msg('INFORME OS CRITÉRIOS DA SUA CONTAGEM')
start = int(input(f'Informe o início da contagem: ').strip())
finish = int(input(f'Informe o fim da contagem: ').strip())
step = int(input(f'Informe o passo da contagem: ').strip())
if step >= 0:
    finish += 1
else:
    finish += -1
counter(start, finish, step)

#### Another way to code ####

################################ SEÇÃO 0 - IMPORTAÇÕES ###################################
import random
from time import sleep
from pprint import pprint
from operator import itemgetter
from datetime import datetime
################################# SEÇÃO 1 - FUNÇÕES ######################################


def contagem(lista):
    i = lista[0]
    f = lista[1]
    if len(lista) == 2:
        if lista[0] > lista[1]:
            p = -1
        else:
            p = 1
    else:
        p = lista[2]
    if f > 0:
        f += 1
    else:
        f -= 1
    if lista[0] > lista[1] and p > 0:
        p = -p
    for n in range(i, f, p):
        print(f'=> {n} ', end='')
        sleep(0.3)
    print()
    print()



def escreva(msg):
    print('=' * (len(msg) + 4))
    print(f'  {msg}')
    print('=' * (len(msg) + 4))
    print()


################################ SEÇÃO 2- CABEÇALHO ######################################
msg = (' *** CONTAGEM *** ')
print('-=-' * 20)
print('{: ^60}'.format(msg))
print('-=-' * 20)
################################ SEÇÃO 3 - VARIÁVEIS #####################################
cor = {'limpa': '\033[m',
       'vermelho': '\033[1:31m',
       'verde': '\033[1:32m',
       'amarelo': '\033[1:33m'}
################################# SEÇÃO 4 - PROGRAMA #####################################
escreva("Contagem de 1 a 10")
contagem([1, 10])
escreva("Contagem de 1 a 10 de 2 em 2")
contagem([1, 10, 2])
escreva("Contagem regressiva")
contagem([10, 1])
print()
escreva("Agora é sua vez !!!")
contagem([int(input('Infome o valor inicial: ')), int(input('Informe o valor final: ')), int(input('Informe o passo: '))])
