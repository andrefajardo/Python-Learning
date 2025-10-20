###  Nessa aula, vamos aprender operações com String no Python.
###  As principais operações que vamos aprender são o Fatiamento de String, Análise com:
###  len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(),
###  title(), strip(), junção com join().


fullName = str(input('Escreva uma frase: ')).strip().upper()
fullNameInvert = fullName[::-1]
lengthName = len(fullName)
letterSearch = str(input('Informe a letra para pesquisa: ')).strip().upper()
print('Na frase, aparecem {} letras {}'. format(fullName.count(letterSearch), letterSearch))
print('A primeira aparece na posição {}.'. format(fullName.find(letterSearch)))
print('A última aparece na posição {}.'. format(lengthName - fullNameInvert.find(letterSearch) -1))
### Or use de simplified form bellow
print('A última aparece na posição {}.'. format(fullName.rfind(fullName)))
