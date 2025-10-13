import math
msg = ' Seno / Cosseno '
button = '='
print('{:=^100}'.format(msg))
angle = float(input('Informe o valor do ângulo: '))
angleRadians = math.radians(angle)
sen = math.sin(angleRadians)
cos = math.cos(angleRadians)
tag = math.tan(angleRadians)
print('A Tangente do ângulo informado é {:.2f}'.format(tag))
print('O seno do ângulo informado é {:.2f}'.format(sen))
print('O cosseno do ângulo informado é {:.2f}'.format(cos))
print('{:=^100}'.format(button))