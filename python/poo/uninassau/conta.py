
class Conta:
    def __init__(self, saldo):
        self.__saldo = saldo

    def depositar(self):
        valor = float(input("Digite um valor a ser depositado: "))
        if valor > 0:
            self.__saldo += valor

    def sacar(self):
        valor = float(input("Digite o valor a ser sacado: "))
        if valor <= self.__saldo:
            self.__saldo -= valor
    
    def get_saldo(self):
        return self.__saldo
    
    def alter_saldo(self, valor):
        self.__saldo += valor
    
class ContaCorrente(Conta):
    def sacar(self):
        taxa = -5
        valor = float(input("Digite o valor a ser sacado: "))
        if valor <= self.get_saldo():
            self.alter_saldo((-(valor) + taxa))

    def imprimir_extrato(self):
        print("O seu saldo atual é:", self.get_saldo())
    
class ContaPoupança(Conta):
    def sacar(self):
        Conta.sacar(self)

    def imprimir_extrato(self):
        print("O seu saldo atual é:", self.get_saldo())

        


if __name__ == "__main__":
    conta_corr = ContaCorrente(100)
    conta_poup = ContaPoupança(100)

    conta_corr.imprimir_extrato()
    
    conta_corr.depositar()
    conta_corr.imprimir_extrato()

    conta_corr.sacar()
    conta_corr.imprimir_extrato()





    