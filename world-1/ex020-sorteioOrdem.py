import random
msg = ' Sorteio da Ordem '
button = '='
print('{:=^100}'.format(msg))
studant1 = (input('Informe o nome do primeiro aluno: '))
studant2 = (input('Informe o nome do segundo aluno: '))
studant3 = (input('Informe o nome do terceiro aluno: '))
studant4 = (input('Informe o nome do quarto aluno: '))
studantList = [studant1, studant2, studant3, studant4]
random.shuffle(studantList)
print('A ordem de apresentação dos alunos é: \n 1° {} \n 2° {} \n 3° {} \n 4° {}'.format(studantList[0], studantList[1], studantList[2], studantList[3]))
print('{:=^100}'.format(button))
