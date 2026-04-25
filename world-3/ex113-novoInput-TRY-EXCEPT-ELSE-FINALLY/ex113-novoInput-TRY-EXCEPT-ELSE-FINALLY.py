################################## SECTION 0 - IMPORTS ###################################

import random
from time import sleep
from datetime import datetime
from wsgiref.validate import validator

from utils import layout
from utils import validation

################################### SECTION 1- HEADER ######################################

layout.header()

################################# SECTION 2 - VARIABLES ####################################

cor = {'limpa': '\033[m',
       'vermelho': '\033[1:31m',
       'verde': '\033[1:32m',
       'amarelo': '\033[1:33m'}

################################# SECTION 3 - CODE #####################################

result = validation.newInput()
print(result)

############################# SECTION 4 - ANOTHER WAY ##################################

# n = validation.leiaInt('Digite um número: ')
# print(f'Você acabou de digitar o número {n}')