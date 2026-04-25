import moeda

value = (input('Informe um valor: ').strip())
tax = (input('Informe um valor para desconto ou aumento: ').strip())

moeda.resume(value, tax)