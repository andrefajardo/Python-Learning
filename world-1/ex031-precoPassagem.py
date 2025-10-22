distance = float(input('Informe a distância da viagem: ').strip())
value = 0
if distance > 200:
    value = distance * 0.45
else:
    value = distance * 0.5
print('Sua passagem custará R$ {:.2f}.'.format(value))