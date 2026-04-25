def increase(value, addValue, formated = True):
    value = float(value.replace(",", "."))
    addValue = float(addValue.replace(",", "."))
    newValue = value + (addValue * value / 100)
    if formated:
        return f'R$ {newValue:.2f}'
    else:
        return newValue

def decrease(value, minusValue, formated = True):
    value = float(value.replace(",", "."))
    minusValue = float(minusValue.replace(",", "."))
    newValue = value - (minusValue * value / 100)
    if formated:
        return f'R$ {newValue:.2f}'
    else:
        return newValue

def half(value, formated = True):
    value = float(value.replace(",", "."))
    newValue = value / 2
    if formated:
        return f'R$ {newValue:.2f}'
    else:
        return newValue

def double(value, formated = True):
    value = float(value.replace(",", "."))
    newValue = value * 2
    if formated:
        return f'R$ {newValue:.2f}'
    else:
        return newValue

def resume(value, tax, formated = True):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \tR$ {(value)}')
    print(f'Dobro do preço: \t{double(value)}')
    print(f'Metade do preço: \t{half(value)}')
    print(f'{tax}% de aumento: \t{increase(value, tax)}')
    print(f'{tax}% de redução: \t{decrease(value, tax)}')