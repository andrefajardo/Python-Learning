################################ SECTION 0 - IMPORTS ###################################

import random
from time import sleep
from datetime import datetime

################################ SECTION 1- HEADER ######################################

frame = '==='
title = ' VOTAÇÃO ELEITORAL '

print( frame * 30)
print('===', ' ' * 84, '===', sep='')
print(f"=== {title:^82} ===")
print('===', ' ' * 84, '===', sep='')
print(frame * 30, '\n')


################################# SECTION 2 - FUNCTIONS ######################################

def msg(txt):
    length = len(txt)
    frame = length + 10
    print(f'#'*frame)
    print(f'{txt:^{frame}}')
    print(f'#'*frame)

def check_vote(year_old):
    current_year = datetime.now().year
    age = current_year - year_old
    if age < 16:
        return 'VOTO NEGADO'
    elif 16 <= age < 18 or age >= 65:
        return 'VOTO OPCIONAL'
    else:
        return 'VOTO OBRIGATÓRIO'

################################ SECTION 3 - VARIABLES #####################################
cor = {'limpa': '\033[m',
       'vermelho': '\033[1:31m',
       'verde': '\033[1:32m',
       'amarelo': '\033[1:33m'}

################################# SECTION 4 - CODE #####################################

age = int(input("Informe o ano de nascimento: "))
print(f'Com base no ano de nascimento {age}, sua condição é de: {check_vote(age)}.\n')

################################# SECTION 5 - ANOTHER WAY #####################################

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


# Programa principal
nasc = int(input("Em que ano você nasceu? "))
print(voto(nasc))
