import random
cpff = str()
validacao = False
while not validacao:
    cpf = str(random.randint(100000000, 999999999))

    soma_1 = 0  # primeira soma
    for c in range(10, 1, -1):
        soma_1 += c * int(cpf[10 - c])

    primeiro_digt = int()
    if 11 - (soma_1 % 11) > 9:
        primeiro_digt = 0
    else:
        primeiro_digt = 1

    cpf += str(primeiro_digt)  # novo cpf com 10 digitos

    soma_2 = 0  # segunda soma
    for c in range(11, 1, -1):
        soma_2 += c * int(cpf[11 - c])
    segundo_digt = 11 - (soma_2 % 11)
    cpf += str(segundo_digt)  # novo cpf com 11 digitos
    cpff = cpf
    break

print(cpff)
