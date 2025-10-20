###  Nessa aula, vamos aprender operações com String no Python.
###  As principais operações que vamos aprender são o Fatiamento de String, Análise com:
###  len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(),
###  title(), strip(), junção com join().


fullName = str(input('Informe o nome completo: ')).strip().upper()
nameSearch = str(input('Informe o termo para pesquisa: ')).strip().upper()
print('O nome possui o termo pesquisado? {}' .format(nameSearch in fullName.split()))