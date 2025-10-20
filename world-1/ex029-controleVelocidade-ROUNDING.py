import math
velCar = float(input('Informe a velocidade do veículo: ').strip())
if velCar >= 80:
    speedingTicket = ( math.floor(velCar)- 80)*7
    print('Você foi multado em R${} por excesso de velocidade.'.format(speedingTicket))
