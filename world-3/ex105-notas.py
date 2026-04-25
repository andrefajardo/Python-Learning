################################ SECTION 0 - IMPORTS ###################################

import random
from time import sleep
from datetime import datetime

################################ SECTION 1- HEADER ######################################

frame = '==='
title = ' ANALISA NOTAS '

print( frame * 30)
print('===', ' ' * 84, '===', sep='')
print(f"=== {title:^82} ===")
print('===', ' ' * 84, '===', sep='')
print(frame * 30, '\n')

################################ SECTION 2 - VARIABLES #####################################

cor = {'limpa': '\033[m',
       'vermelho': '\033[1:31m',
       'verde': '\033[1:32m',
       'amarelo': '\033[1:33m'}

################################# SECTION 3 - FUNCTIONS ######################################

def msg(txt):
    length = len(txt)
    frame = 50
    print(f'#'*frame)
    print(f'{txt:^{frame}}')
    print(f'#'*frame)

def grades(* grade, status = False):
    """
    -> Função para analisar notas e situação de um aluno.
    :param grade: Uma ou mais notas do aluno (aceita várias).
    :param status: Valor opcional, indicando se deve ou não adicionar a situação.
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    grades = sorted(grade)
    average = sum(grade) / len(grade)
    print(f'Analisando as notas...')
    sleep(0.3)
    result = f'Ao todo foram informadas {len(grade)} notas.'
    result += f'\nA maior nota foi {grades[-1]:.1f}.'
    result += f'\nA menor nota foi {grades[0]:.1f}.'
    result += f'\nA média das notas foi {average:.2f}.'
    if status:
        if average >= 7:
            result += f'\nO aluno está {cor["verde"]}APROVADO{cor["limpa"]}!'
        elif 5 <= average < 7:
            result += f'\nO aluno está de {cor["amarelo"]}RECUPERAÇÃO{cor["limpa"]}.'
        else:
            result += f'\nO aluno está {cor["vermelho"]}REPROVADO{cor["limpa"]}!'
    return result


################################# SECTION 4 - CODE #####################################
help(grades)
result = grades(5.5, 5.0, 0.0, 4.5, status=True)
msg(result)

############################# SECTION 5 - ANOTHER WAY ##################################

def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


# Programa Principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)