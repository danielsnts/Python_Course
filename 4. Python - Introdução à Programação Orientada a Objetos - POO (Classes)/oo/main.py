from teste_conta import *

if __name__ == '__main__':
    conta = cria_conta('1554-5', 'John Steve', 1222.00, 2000.00)
    deposita(conta, 3000.00)
    extrato(conta)
