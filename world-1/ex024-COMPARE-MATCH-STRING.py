###  Nessa aula, vamos aprender operações com String no Python.
###  As principais operações que vamos aprender são o Fatiamento de String, Análise com:
###  len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(),
###  title(), strip(), junção com join().

city = str(input('Informe o nome da cidade: ')).strip()
cityVector = city.split()
print('O nome da cidade começa com a palavra "Santo"? ')
print('Santo' in city.title())
print('Santo' == city[0:5].title())
