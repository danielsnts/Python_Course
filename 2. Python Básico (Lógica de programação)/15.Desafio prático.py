
nome = str(input('Insira seu nome: '))

idade = int(input('Insira sua idade: '))
peso = int(input('Insira seu peso em quilogramas: '))
altura = float(input("Insira sua altura em metros: "))
ano = str(int(input('Insira seu ano de nascimento: ')))
imc = peso/(altura*altura)

print(nome + " tem " + str(idade) + " anos, " + str(altura) + " de altura e pesa " + str(peso) + "kg.")
print("O IMC de " + nome + " é " + str(imc) + ".")
print(nome + " nasceu em " + ano + ".")
