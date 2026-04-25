from utils import currency, validation

value = (input('Informe um valor: ').strip())
tax = (input('Informe um valor para desconto ou aumento: ').strip())

if validation.validData(value) and validation.validData(tax):
    currency.resume(validation.validData(value), validation.validData(tax))
else:
    print('Valor inválido. Por favor, insira um número válido.')

