"""
1º
"""

"""numero = input("Digite um número inteiro: ")

if numero.isnumeric():
    numero = int(numero)

    if numero % 2 == 0:
        print("PAR")
    else:
        print("IMPAR")
else:
    print("Is not a number!")"""

"""horas = input("Hora: ")
hora = int(horas[0:2])

if hora >= 0 or hora <= 11:
    print("Bom dia!")
elif hora >= 12 or hora <= 17:
    print("Boa tarde")
elif hora >= 18 or hora <= 23:
    print("Boa noite!")"""

nome = input("Insira seu nome")

if len(nome) <= 4:
    print("Nome curto")
elif len(nome) <= 6:
    print("NOme normal")
else:
    print("Nome muito grande!")
