################################ SECTION 1- HEADERS ######################################

from .. import constants

def header(title):
    frame = '==='
    print(frame * 30)
    print('===', ' ' * 84, '===', sep='')
    print(f"=== {title:^82} ===")
    print('===', ' ' * 84, '===', sep='')
    print(frame * 30, '\n')

def msg(txt, option_list="1"):
    length = len(txt)
    frame = length + 20
    print(f'#'*frame)
    print(f'{txt:^{frame}}')
    print(f'#'*frame)
    for i, item in enumerate(option_list, start=1):
            print(f'{constants.colors["amarelo"]}  {i} - {constants.colors["verde"]}{item}. {constants.colors["limpa"]}')
    print(f'#' * frame, '\n')

def sub_header(txt):
    length = len(txt)
    frame = length + 20
    print(f'#'*frame)
    print(f'{txt:^{frame}}')
    print(f'#'*frame, '\n')