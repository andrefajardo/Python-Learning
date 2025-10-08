num = int(input('Informe um valor em metros: '))
valorCm = num * 100
valorMm = num * 1000
print('O valor {:.2f}m corresponde ao valor {:.2f}cm e ao valor {:.2f}mm' .format(num, valorCm, valorMm))