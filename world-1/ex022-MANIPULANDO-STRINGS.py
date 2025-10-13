###  Nessa aula, vamos aprender operações com String no Python.
###  As principais operações que vamos aprender são o Fatiamento de String, Análise com:
###  len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(),
###  title(), strip(), junção com join().

name = str(input('Digite seu nome completo: ')).strip()
print('Nome com Maiúculas: ', name.upper())
print('Nome com Minúsculas: ', name.lower())
nameSplit = name.split()
print('Seu primeiro nome é {} e ele tem {} letras' .format((nameSplit[0]), (len(nameSplit[0]))))
## You can change this part bellow using " - name.count(' ')" that will return the number of spaces
nameJoin = ''.join(nameSplit)
print('Seu primeiro nome todo tem {} letras' .format(len(nameJoin)))