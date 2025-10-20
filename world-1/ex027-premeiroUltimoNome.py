###  Nessa aula, vamos aprender operações com String no Python.
###  As principais operações que vamos aprender são o Fatiamento de String, Análise com:
###  len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(),
###  title(), strip(), junção com join().

fullName = str(input('Escreva seu nome completo: ')).strip().upper()
fullName = fullName.split()
fullNameLength = len(fullName)
print('Seu primeiro nome é: {} e o seu último nome é {}.'.format(fullName[0], fullName[fullNameLength -1]))
