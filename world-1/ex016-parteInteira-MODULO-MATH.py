## import math ( if used, remember to put the math.trunc(num) instead trunc(num) )
from math import trunc
num = float(input('Informe um número racional: '))
## intPart = math.trunc(num)
intPart = trunc(num)
print('A parte inteira do número informado é: {}'.format(intPart))