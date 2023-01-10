class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor > self.saldo + self.limite:
            print("Limite insuficiente")
            return False
        else:
            self.saldo -= valor
            print("Saque realisado."
                  f"Saldo atual: R$ {self.saldo:,.2f}")
            return True

    def deposita(self, destino, valor):
        valor_retirado = self.sacar(valor)
        if valor_retirado:
            return True
        else:
            return False


    def extrato(self):
        print(f'Conta: {self.numero}\n'
              f'Saldo: R$ {self.saldo:,.2f}'  # Formatação para dinheiro
              )
