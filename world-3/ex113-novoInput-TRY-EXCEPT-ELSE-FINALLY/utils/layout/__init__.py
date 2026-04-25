################################ SECTION 1- HEADERS ######################################

cor = {'limpa': '\033[m',
       'vermelho': '\033[1:31m',
       'verde': '\033[1:32m',
       'amarelo': '\033[1:33m'}

def header():
    frame = '==='
    title = ' ANALISA INTEIRO '

    print(frame * 30)
    print('===', ' ' * 84, '===', sep='')
    print(f"=== {title:^82} ===")
    print('===', ' ' * 84, '===', sep='')
    print(frame * 30, '\n')

def msg(txt):
    length = len(txt)
    frame = length + 10
    print(f'#'*frame)
    print(f'{txt:^{frame}}')
    print(f'#'*frame)

#######################################################################################