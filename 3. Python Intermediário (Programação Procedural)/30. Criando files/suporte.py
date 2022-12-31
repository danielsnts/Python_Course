universidades = ['CEFET', 'UENF', 'UERJ', 'UFF', 'UFRJ', 'UFRRJ', 'UNIRIO']
cursos = [
    'BIOLOGIA',
    'FÍSICA',
    'GEOGRAFIA',
    'HISTÓRIA',
    'LETRAS',
    'MATEMÁTICA',
    'PEDAGOGIA',
    'QUIMICA',
    'TURISMO',
    'COMPUTAÇÃO',
    'GESTÃO EM TURISMO',
    'SEGURANÇA PÚBLICA',
    'ADMINISTRAÇÃO',
    'ADMINISTRAÇÃO PÚBLICA',
    'CIÊNCIAS CONTÁBEIS',
    'ENGENHARIA METEOROLÓGICA',
    'ENGENHARIA DE PRODUÇÃO'
]
polos = [
    "Angra dos Reis",
    "Barra do Piraí",
    'Belford Roxo',
    'Bom Jardim',
    'Bom Jesus do Itabapoana',
    'Cardoso Moreira',
    'Cabo Frio',
    'Campo Grande',
    'Cantagalo',
    'Duque de Caxias',
    'Itaguai',
    'Itaocara',
    'Itaperuna',
    'Macaé',
    'Magé',
    'Mangaratiba',
    'Mesquita',
    'Miguel Pereira',
    'Miracema',
    'Natividade',
    'Niterói',
    'Nova Friburgo',
    'Nova Iguaçu',
    'Paracambi',
    'Petrópolis',
    'Pinheiral',
    'Piraí',
    'Quatis',
    'Resende',
    'Rio Bonito',
    'Rio das Flores',
    'Rio das Ostras',
    'Rocinha',
    'Santa Maria Madalena',
    'São Fidélis',
    'São Francisco de Itabapoana',
    'São Gonçalo',
    'São Pedro da Aldeia',
    'Saquarema',
    'Teresópolis',
    'Três Rios',
    'Volta Redonda'
]


def num_inscricao(linha_toda=''):  # Recebe a linha e retorna o nomero e inscrição
    lista_da_linha = linha_toda.split()
    return str(lista_da_linha[0])


def cpf(linha_toda2):  # Recebe a linha e retorna o cpf
    lista_da_linha2 = linha_toda2.split()
    return str(lista_da_linha2[1])


def nome(linha_toda3):  # Recebe a linha e retorna o nome
    lista_da_linha3 = linha_toda3.split()
    return str(lista_da_linha3[2])


def universidade(linha_toda_4='', todas_universisades=[]):
    universidade_selecionada = str()
    for instituicao in todas_universisades:
        if str(instituicao) in linha_toda_4:
            universidade_selecionada = str(instituicao)
            break

    return universidade_selecionada


def polo(linha_toda_5='', todos_polos=[]):
    polo_selecionado = str()
    for polo in todos_polos:
        if str(polo) in linha_toda_5:
            polo_selecionado = str(polo)
            break

    return polo_selecionado


def notas(linha_toda_6=''):
    nota = str()
    nova_lista = linha_toda_6.split()
    for item in nova_lista:
        if ',' in str(item):
            nota = item
            break
        else:
            nota = '0'
    nota = float(nota.replace(',', '.'))
    return nota


def curso(linha_toda7='', todos_cursos=[]):
    curso_selecionado = str()
    for curso in todos_cursos:
        if str(curso) in linha_toda7.upper():
            curso_selecionado = str(curso)
            break

    return curso_selecionado
