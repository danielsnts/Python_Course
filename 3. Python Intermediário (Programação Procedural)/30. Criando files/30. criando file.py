with open('abc.txt', 'r', encoding="utf-8") as file:  # Tem acentos no arquivo
    file.seek(0, 0)
    linhas = file.readlines()

from itertools import groupby
from suporte import *


linha = '0000054 122.xxx.xxx-03 RICARDO Matemática Nova Iguaçu UFF 24,0 HABILITADO CORREÇÃO REDAÇÃO'

"""print(nome(linha))
print(cpf(linha))
print(num_inscricao(linha))
print(universidade(linha, universidades))
print(polo(linha, polos))
print(notas(linha))
print(curso(linha, cursos))"""

inscritos = []
for linha in linhas:
    item = {}
    item['INSCRIÇÂO'] = num_inscricao(linha)
    item['CPF OCULTO'] = cpf(linha)
    item['PRIMEIRO NOME'] = nome(linha)
    item['CURSO'] = curso(linha, cursos)
    item['POLO'] = polo(linha, polos)
    item['INSTITUIÇÃO'] = universidade(linha, universidades)
    item['NOTA'] = notas(linha)
    inscritos.append(item)

# print(f"Tamnho de Inscritos: {len(inscritos)}")

rocinha = []

for i in inscritos:
    if i['POLO'] == 'Rocinha':
        rocinha.append(i)

computacao = []  # Onde meus concorrentes são armazenados

for i in rocinha:
    if i['CURSO'] == 'COMPUTAÇÃO':
        computacao.append(i)

computacao.sort(key=lambda item: item['NOTA'])

"""for o, i in enumerate(computacao):
    print(f"{155-o} {i['INSCRIÇÂO']:6.0f} {i['PRIMEIRO NOME']} nota: {i['NOTA']}" )"""

with open('redacao.txt', 'r', encoding="utf-8") as file:  # Abrindo e lendo o arquivo redacao.txt
    file.seek(0, 0)
    linhas = file.readlines()


notas_redacao = []  # Guarda as notas de redação
for linha in linhas:
    aux = linha.split()
    if aux[0].isnumeric() and len(aux[0]) == 7:  # Seleciona apenas as linhas que interessa no arquivo
        inscrito = {}  # DIcionario que ira receber o numero de inscricao e a respectiva nota
        inscrito['INSCRIÇÂO'] = aux[0]  # Recebe o numero de inscricao
        inscrito['NOTA_REDACAO'] = float(aux[-4].replace(',', '.'))  # Recebe o numero de inscricao
        notas_redacao.append(inscrito)


nota_final = []
for i in computacao:

    for o in notas_redacao:
        if i['INSCRIÇÂO'] == o['INSCRIÇÂO']:
            aux = {}
            aux['INSCRIÇÂO'] = i['INSCRIÇÂO']
            aux['NOME'] = i['PRIMEIRO NOME']
            aux['nota_1'] = i['NOTA']
            aux['nota_2'] = o['NOTA_REDACAO']
            aux['nota_final'] = i['NOTA'] + 0.37 * o['NOTA_REDACAO']
            nota_final.append(aux)

nota_final.sort(key=lambda item: item['nota_final'])
for o, i in enumerate(nota_final):
    print(f"{76 - o} - {i['INSCRIÇÂO']} {i['NOME']} {i['nota_1']} + 0,37 * {i['nota_2']} = {i['nota_final']}")
