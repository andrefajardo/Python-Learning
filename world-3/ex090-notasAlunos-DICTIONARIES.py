##################################################################################################
###
###     Curso em Vídeo - Curso de Python - Mundo 3
###     Prof. Gustavo Guanabara
###
###     Module 3 Description: A set of exercises about data structure, functions, modules and
###     package, error handling, etc.
###
###     student:  André Fajardo
###
##################################################################################################
####################################   Imported Modules  #########################################

# Import exemples
# from datetime import datetime
# from itertools import count

######################################  Inicial Label  ###########################################
frame = '==='
title = ' MEDIA DE ALUNOS '

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
student = dict()
situation = ''
########################################### Code #################################################
name = str(input('Nome do Aluno: ').strip().upper())
average = float(input('Média do Aluno: ').strip())
if average < 5.0:
    situation = 'REPROVADO'
elif (5.0 <= average) and (average <= 7.0):
    situation = 'EM RECUPERAÇÃO'
else:
    situation = 'APROVADO'

student['Nome'] = name
student['Média do Aluno'] = average
student['Situação'] = situation

print(f'\n{colors["backYellow"]}{" RESULTADO FINAL ":^84}{colors["clean"]}\n')
for k, v in student.items():
    print('-'*30)
    print(f'{k}: {v}')