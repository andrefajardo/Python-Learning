from datetime import date
year = int(input('Informe um ano qualquer: ').strip())
if year == 0:
    year = date.today().year
if year % 4 == 0:
    if (year % 100 == 0) & (year % 400 != 0):
        print('O ano informado "{}" NÃO é bissexto.'.format(year))
    else:
        print('O ano informado "{}" É bissexto.'.format(year))
else:
    print('O ano informado "{}" NÃO é bissexto.'.format(year))