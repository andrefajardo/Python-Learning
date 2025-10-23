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
title = ' VALOR PAGAMENTO '

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

price = float(input('Informe o valor do produto: ').strip())
option = int(input('Informe a condição de pagamento: \n'
                   '1 - À vista em dinheiro; \n'
                   '2 - À vista no cartão; \n'
                   '3 - Duas vezes no cartão; \n'
                   '4 - Três ou mais vezes no cartão. \n'
                   'Opção: ').strip())

print('********************************************************************************')
if option == 1:
    print('Você terá 10% de desconto e pagará R$ {}.'.format(price - price * 10 /100))
elif option == 2:
    print('Você terá 5% de desconto e pagará R$ {}.'.format(price - price * 5 /100))
elif option == 3:
    print('Não há desconto para está forma de pagamento.')
elif option == 4:
    print('Você terá 20% de acréscimo e pagará R$ {}.'.format(price + price * 20 /100))
else:
    print('Opção INVÁLIDADE. Tente novamente.')
print('********************************************************************************')
