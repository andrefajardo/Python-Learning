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

from random import randint

######################################  Inicial Label  ###########################################
frame = '==='
title = ' TABELA DE PREÇOS '

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
products =''
########################################### Code #################################################

while True:
    print('Informe o nome e o preço dos produtos:\n')
    productName = str(input('Informe o nome do produto: ').strip().upper())
    productPrice = int(input('Informe o preço do produto: ').strip())
    products += (f'{productName}-{productPrice}-')
    option = ' '
    while option not in 'SN':
        option = str(input('Gostaria de continuar? [S/N]: \n').strip().upper()[0])
    if option == 'N':
        break

productsLength = len(products)
products = products[:productsLength - 1]  ### extracting the last "-" with "-1".
products2 = products.split('-')
products3 = tuple(products2)

print(f'=+='*30)
print(' RELAÇÃO DOS PRODUTOS E PREÇOS '.center(90, ' '))
print(f'=+='*30)

# 2. Definitions of formation
totalwidth = 90  # Total width

try:
    for count in range(0, productsLength, 2):
        product = products3[count]  # Current item (Product)
        price = products3[count + 1]  # Next item (Price)
        price_str = f'R$ {float(price):.2f}' # Very interesting way to format before
        charLength = totalwidth - (len(product) + len(price) + 8)
        print(f'{product:<} {"-" * charLength} R$ {float(price):.2f}')
        print(f'{product:<} {"-" * charLength} {price_str}')

except IndexError:
    print(' ACABOU '.center(90, '='))

print('\n')

### Another way to format
print(' OUTRO FORMA DE EXIBIÇÃO '.center(90, '='))

print('-' * 40)
print(f'{"Listagem de Preços":^40}')
print('-' * 40)
for pos in range(0, len(products3)):
    if pos % 2 == 0:
        print(f'{products3[pos]:.<30}', end='')
    else:
        print(f'R$ {float(products3[pos]):>7.2f}')
