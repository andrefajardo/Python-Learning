
cor = {'limpa': '\033[m',
       'vermelho': '\033[1:31m',
       'verde': '\033[1:32m',
       'amarelo': '\033[1:33m'}

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor

def newInput():
    """
    -> Solicita ao usuário que digite um número entre 1 e 100000.
    """
    while True:
        try:
            n = int(input('Digite um número entre 1 e 100000: '))
        except ValueError as erro:
            print(f'{cor["vermelho"]}VALOR INVÁLIDO! Erro: {erro}{cor["limpa"]} ')
            continue
        except EOFError as erro:
            print(f'{cor["vermelho"]}VALOR INVÁLIDO! Erro: {erro}{cor["limpa"]} ')
            return 'Encerrando o programa...'
        else:
            if 1 <= n <= 100000:
                n = f'{cor["verde"]}Você digitou o número: {n}.{cor["limpa"]}'
                return n
            else:
                print(f'{cor["vermelho"]}VALOR FORA DO INTERVALO! Digite um número entre 1 e 100000.{cor["limpa"]}')
                break
        finally:
            print(f'{cor["amarelo"]}Processamento concluído.{cor["limpa"]}')