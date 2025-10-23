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
title = ' CÁLCULO DA MÉDIA DO ALUNO '

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

grade1 = float(input('Informe o valor da primeira nota: ').strip())
grade2 = float(input('Informe o valor da segunda nota: ').strip())
gradeAverage = (grade1 + grade2)/2
if gradeAverage >= 7:
    print('Média "{}". O aluno foi {}APROVADO{}. Parabéns!'.format(gradeAverage, colors['greenBold'], colors['clean']))
elif gradeAverage < 5:
    print('Média "{}". O aluno foi {}REPROVADO{}.'.format(gradeAverage, colors['redBold'], colors['clean']))
else:
    print('Média "{}". O aluno está em {}RECUPERAÇÃO{}.'.format(gradeAverage, colors['backYellow'], colors['clean']))

