import random
from time import sleep
print('Vou pensar em um número de 0 a 5 e você deve tentar adivinhar qual é o número.')
numSort = random.randint(1, 3)
num = int(input('Escolha um número de 1 a 3: ').strip())
print('=+='*20)
print("PENSANDO...")
print('=+='*20)
sleep(3)
if num == numSort:
	print('Parabéns, você acertou o número!')
else:
	print('Que pena! Você errou. O número era {}'.format(numSort))
