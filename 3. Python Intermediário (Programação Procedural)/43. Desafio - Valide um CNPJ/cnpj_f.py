import re

REGRESSIVO = (6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)


def apenas_numeros(cnpj):  # Deixa apenas os números no cnpj
    return re.sub(r'[^0-9]', '', cnpj)


def proximo_digito(cnpj=''):
    soma = 0

    if 12 == len(cnpj):
        for i, numero in enumerate(cnpj):
            soma += REGRESSIVO[i + 1] * int(numero)
    elif 13 == len(cnpj):
        soma = 0
        for i, numero in enumerate(cnpj):
            soma += REGRESSIVO[i] * int(numero)

    numero = 11 - (soma % 11)
    numero = numero if numero < 10 else 0
    return str(numero)

def valida(cnpj, novo_cnpj):
    if cnpj == novo_cnpj:
        print(f'O CNPJ {cnpj} é válido')
    else:
        print(f'O CNPJ {cnpj} é inválido')
