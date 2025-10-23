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
title = ' ALISTAMENTO MILITAR '

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

bonrDateStg= str(input("Digite sua data de nascimento (dd/mm/aaaa): \n").strip())
bornDate = datetime.strptime(bonrDateStg, "%d/%m/%Y").date()
currentDate = datetime.today().date()
yearsOld = relativedelta(currentDate, bornDate)
### print(yearsOld)
print('Atualmente, você tem: \n'
      '* {} anos;\n'
      '* {} meses;e\n'
      '* {} dias.\n'.format(yearsOld.years, yearsOld.months, yearsOld.days))

yearMilitaryDuty = currentDate.year - bornDate.year
if yearMilitaryDuty == 18:
    print('Você deverá se alistar neste ano.')
elif yearMilitaryDuty < 18:
    print('Você deverá se alistar daqui há {} ano(s).'. format(18 - yearMilitaryDuty))
else:
    print('Você deveria ter se alistdo há {} ano(s).'.format(yearMilitaryDuty - 18))

