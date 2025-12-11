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

from random import randint
from random import sample
from time import sleep

######################################  Inicial Label  ###########################################
frame = '==='
title = ' BOLETIM ESCOLAR '

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
grades = list()
student = ' '
reportCard = list()
count = 1
########################################### Code #################################################
while True:
    student = str(input(f'Informe o nome do aluno: ').strip().upper())
    grades.append(student)
    grades.append([float(input('Informe a primeira nota: ')), float(input('Informe a segunda nota: '))])
    reportCard.append(grades[:])
    grades.clear()
    student = ''
    option = ' '
    while option not in 'SN':
        option = str(input('Gostaria de continuar? [S/N]: \n').strip().upper()[0])
    if option == 'N':
        break

print(reportCard)
print(f'\n{" BOLETIM FINAL ":=^50}\n')
print(f'{"Nº":<4}{"NOME":<15}{" N-1    N-2":<9}{"MÉDIA":>20}')
print('='*50)
for student in reportCard:
    average = (student[1][0] + student[1][1]) / 2
    print(f'{count:<4}{student[0]:<15}{student[1][0]:<7.2f}{student[1][1]:<7.2f}{average:>17.2f}')
    count += 1
    print('='*50)


print(f'\nSelecione um aluno para ver suas notas detalhadas.\n')
print('='*50)
while True:
    studentName = str(input('Informe o nome do aluno (ou "999" para sair): ').strip().upper())
    if studentName == '999':
        print('\nFinalizando o programa... Até logo!')
        break
    found = False
    for student in reportCard:
        if student[0] == studentName:
            print('=' * 50)
            print(f'As notas de {studentName} são: N-1: {student[1][0]:.2f} e N-2: {student[1][1]:.2f}')
            print('=' * 50)
            found = True
    if not found:
        print(f'Aluno {studentName} não encontrado. Tente novamente.')

