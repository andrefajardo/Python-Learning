import math
msg = ' Hipotenuza '
button = '='
print('{:=^100}'.format(msg))
cat1 = float(input('Informe o primeiro cateto: '))
cat2 = float(input('Informe o segundo cateto: '))
hip = (math.sqrt(cat1**2 + cat2**2))
hip2 = math.hypot(cat1, cat2)
print('A hipotenuza do triângulo formado pelos dois catetos informados é {:.2f}'.format(hip))
print('A hipotenuza do triângulo formado pelos dois catetos informados é {:.2f}'.format(hip2))
print('{:=^100}'.format(button))
