###  Nessa aula, vamos aprender operações com String no Python.
###  As principais operações que vamos aprender são o Fatiamento de String, Análise com:
###  len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(),
###  title(), strip(), junção com join().


num= int(input('Digite um número de 0 a 9999: '))
mil = num // 1000
print('O número possui {} milhares: '.format(mil))
num = num % 1000
cen = num // 100
print('O número possui {} centenas: '.format(cen))
num = num % 100
dec = num // 10
print('O número possui {} dezenas: '.format(dec))
num = num % 10
uni = num // 1
print('O número possui {} unidades: '.format(uni))