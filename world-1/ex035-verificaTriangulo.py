
### The code formatation ASCII is: \033["cod style";"cod text color";"cod background color"m

colors = {
    'BackGren':'\033[0;;42m',
    'BackYellow':'\033[0;;43m',
    'red':'\033[0;31m',
    'redBold':'\033[1;31m',
    'blue':'\033[0;34m',
    'inverted':'\033[7m',
    'clean':'\033[m'
}
side1 = float(input('Informe o primeiro lado do triângulo: ').strip())
side2 = float(input('Informe o segundo lado do triângulo: ').strip())
side3 = float(input('Informe o terceiro lado do triângulo: ').strip())

setSides = [side1, side2, side3]
setSides.sort()

if (setSides[0] + setSides[1]) < setSides[2]:
    print('As medidas informadas {}NÃO FORMAM{} um triângulo.'.format(colors['redB'], colors['clean']))
else:
    print('As medidas informadas {}FORMAM{} um triângulo.'.format(colors['inverted'], colors['clean']))