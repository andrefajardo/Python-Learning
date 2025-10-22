import math
initSal = float(input('Informe o valor atual do salário: ').strip())
if initSal > 1250:
    increaseSal = ( math.floor(initSal) * 10 / 100)
    print('Seu salário terá um reajuste de R$ {} e totalizará R$ {}.'.format(increaseSal, initSal + increaseSal))
else:
    increaseSal = (math.floor(initSal) * 15 / 100)
    print('Seu salário terá um reajuste de R$ {} e totalizará R$ {}.'.format(increaseSal, initSal + increaseSal))