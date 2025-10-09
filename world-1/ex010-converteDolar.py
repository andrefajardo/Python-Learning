num = float(input('Informe um valor que possui em reais: R$ '))
cambio = 3.27
totalDolar = num // cambio
restoReal = num % cambio
print('Com o valor de R$ {:.2f} (reais), poderá ser adquirido o valor de ${:.2f} (dolar(es)). \nRestarão R$ {:.2f} (reais)' .format(num, totalDolar, restoReal))