import random
import re
from random import randint

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
        return True
    else:
        return False



validacao = False
while not validacao:

    cnpj = str(random.randint(10000000000000, 99999999999999))

    novo_cnpj = apenas_numeros(cnpj[0:12])
    novo_cnpj += proximo_digito(novo_cnpj)
    novo_cnpj += proximo_digito(novo_cnpj)  # Calcula um novo cnpj a partir dos 12 primeiros algarismos

    validacao = True if valida(cnpj, novo_cnpj) else False


tela = f'{cnpj[0:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}'
#04.252.011/0001-10
print(tela)