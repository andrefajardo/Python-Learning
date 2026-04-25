
import requests
from .. import layout


def searchURL(timeout=5):
    """
    -> Solicita ao usuário que digite uma URL, para verificar a existência.
    """
    while True:
        try:
            url = str(input('Digite uma URL para pesquisa: ').strip())
            requests.head(url, allow_redirects=True, timeout=timeout)
        except ValueError as erro:
            print(f'{layout.cor["vermelho"]}URL INVÁLIDO! Erro: {erro}{layout.cor["limpa"]} ')
            continue
        else:
            resp = f'{layout.cor["verde"]}Você acessou o site: {url}.{layout.cor["limpa"]}'
            return resp
        finally:
            print(f'{layout.cor["amarelo"]}Pesquisa concluída.{layout.cor["limpa"]}')
