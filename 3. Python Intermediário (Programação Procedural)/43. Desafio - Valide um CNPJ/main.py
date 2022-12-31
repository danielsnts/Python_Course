from cnpj_f import *

cnpj_s = [
    '04.252.011/0001-10',
    '40.688.134/0001-61',
    '71.506.168/0001-11',
    '12.544.992/0001-05'
]


while True:
    cnpj = input('Insira um CNPJ: ')
    novo_cnpj = apenas_numeros(cnpj[0:12])
    novo_cnpj += proximo_digito(novo_cnpj)
    novo_cnpj += proximo_digito(novo_cnpj)  # Calcula um novo cnpj a partir dos 12 primeiros algarismos

    valida(cnpj, novo_cnpj)
