import random
msg = ' Sorteio '
button = '='
print('{:=^100}'.format(msg))
studant1 = (input('Informe o nome do primeiro aluno: '))
studant2 = (input('Informe o nome do segundo aluno: '))
studant3 = (input('Informe o nome do terceiro aluno: '))
studant4 = (input('Informe o nome do quarto aluno: '))
studantList = [studant1, studant2, studant3, studant4]
studant = random.choice(studantList)
print('O aluno sorteado foi o(a) {}'.format(studant))
print('{:=^100}'.format(button))