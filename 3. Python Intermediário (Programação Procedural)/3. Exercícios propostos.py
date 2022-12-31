# 1
"""def saudacao(msg="Olá", nome="Daniel"):
    print(msg + ", " + nome)


saudacao("Oi", "Daniel")
"""

"""# 2


def soma(a=1, b=2, c=3):
    resultado = a + b + c
    return resultado


print(soma(2, 2, 22))"""

"""# 3


def incremento(valor=100, aumento=10):
    return valor * (1 + aumento/100)


print(incremento(1111, 10))"""

# 4

def fizzbuzz(numero = 30):
    if numero % 15 == 0:
        print("Fizz Buzz")
    elif numero % 5 == 0:
        print("Buzz")
    elif numero % 5 == 0:
        print("Fizz")

fizzbuzz(55)