larg = float(input('Informe a largura da parede: '))
comp = float(input('Informe o comprimento da parede: '))
area = larg * comp
totalTinta = area / 2
print('Para uma área de {:.2f}m, serão necessários {:.2f} litros de tinta.' .format(area, totalTinta))