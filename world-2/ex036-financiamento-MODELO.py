###################################################################################################
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

import math
from time import sleep

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

propertyValue = float(input('Informe o valor do imóvel desejado: R$ ').strip())
salaryValue = float(input('Informe o valor da sua renda bruta: R$ ').strip())
paymentTime = int(input('Informe o tempo desejado para quitar a dívida (anos): ').strip())

print('ANALISANDO...')
sleep(2)

installments = propertyValue / (paymentTime * 12)
maxInstallment = salaryValue * 30 / 100

print(installments)
print(maxInstallment)

if maxInstallment < installments:
    print('Infelizmente o valor do financiamento (R$ {:.2f}) é superior a 30% do seu salário.\n'
          'O Empréstimo foi {}NEGADO{}.'.format(installments, colors['redBold'], colors['clean']))
else:
    print('O valor do financiamento (R$ {:.2f}) é inferior a 30% do seu salário.\n'
          'O Empréstimo foi {}APROVADO{}.'.format(installments, colors['greenBold'], colors['clean']))