string = 'zxcvbnmasd01234567890123456789012345678901234567890123456789012345678901234567890123456789qwertyuiop'
lista = [string[i:i+10] for i in range(0, len(string), 10)]

resultado = '.'.join(lista)
print(resultado)

"""for c in range(0, tamanho_string, 10):
    print(string[c:c+10])
    lista.append(string[c:c+10])
print(f'Lista de tamanho {len(lista)}: {lista} ')"""
