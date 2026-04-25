import moeda

value = input('Informe um valor: ').strip()
addValue = input('Informe um valor para desconto ou aumento: ').strip()
print(f'O valor acrescido é: {moeda.increase(value, addValue)}')
print(f'O valor reduzido é: {moeda.decrease(value, addValue)}')
print(f'A metade do valor é: {moeda.half(value)}')
print(f'O dobro do valor é: {moeda.double(value)}')