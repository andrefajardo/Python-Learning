km = float(input('Informe a quantidade de km rodados: '))
days = float(input('Informe a quantidade de dias alocados: '))
txday = 60
txkm = 0.15
totalValue = (txkm * km) + (txday * days)
label = ' Py - Locadora '
button = ' By Fajardo =='
# textin format and centralization #
print('{:=^100}'.format(label))
print('O total de gastos com o veículo, considerando os {}km rodados nos {} dias é de: R$ {:.2f}.'.format(km, days, totalValue))
print('{:=>100}'.format(button))
print('{:=<100}'.format(button))