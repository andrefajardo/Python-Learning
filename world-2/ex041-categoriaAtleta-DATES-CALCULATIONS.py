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
title = ' CATEGORIA DO ATLETA '

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

from datetime import datetime
from dateutil.relativedelta import relativedelta

########################################### Code #################################################

birthDate = str(input('Informe sua data de nascimento (DD/MM/AAAA): ').strip())
birthDate = datetime.strptime(birthDate, "%d/%m/%Y").date()
currentDate = datetime.today()
yearsOld = relativedelta(currentDate, birthDate)

print(yearsOld.years)

if yearsOld.years > 20:
    print('O atleta pertence à categoria {}MASTER{}.'.format(colors['greenBold'], colors['clean']))
elif yearsOld.years > 19:
    print('O atleta pertence à categoria {}SÊNIOR{}.'.format(colors['greenBold'], colors['clean']))
elif yearsOld.years > 14:
    print('O atleta pertence à categoria {}JUNIOR{}.'.format(colors['greenBold'], colors['clean']))
elif yearsOld.years > 9:
    print('O atleta pertence à categoria {}INFANTIL{}.'.format(colors['greenBold'], colors['clean']))
else:
    print('O atleta pertence à categoria {}MIRIN{}.'.format(colors['greenBold'], colors['clean']))