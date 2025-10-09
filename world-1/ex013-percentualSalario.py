salario = float(input('Informe o valor do salário: '))
percentual = 15
valorAumento = salario * percentual / 100
print('O percentual de aumento é de {:.2f}%. \nO novo valor é de R$ {:.2f}.' .format(percentual, (salario + valorAumento)))