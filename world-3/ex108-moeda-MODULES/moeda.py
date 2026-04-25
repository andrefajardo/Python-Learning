def increase(value, addValue, formated = True):
    newValue = value + (addValue * value / 100)
    if formated:
        return f'R$ {newValue:.2f}'
    else:
        return newValue

def decrease(value, minusValue, formated = True):
    newValue = value - (minusValue * value / 100)
    if formated:
        return f'R$ {newValue:.2f}'
    else:
        return newValue

def half(value, formated = True):
    newValue = value / 2
    if formated:
        return f'R$ {newValue:.2f}'
    else:
        return newValue

def double(value, formated = True):
    newValue = value * 2
    if formated:
        return f'R$ {newValue:.2f}'
    else:
        return newValue