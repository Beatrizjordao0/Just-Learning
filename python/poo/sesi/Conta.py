
class ContaBancaria:
    def __init__(self, numero_conta, saldo, titular):
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.titular = titular

    def depositar(self, ):
        self.saldo = int(self.saldo)
        print('Seu saldo é: ', self.saldo)
        deposito = int(input('Quanto você quer depositar?'))
        self.saldo += deposito   
        print(f'Você depositou {deposito} na sua conta. seu saldo agora é de {self.saldo}')

    def sacar(self):
        self.saldo = int(self.saldo)
        saque = int(input('Quanto você quer sacar?'))
        if saque > self.saldo:
            print('Você não pode sacar. Saldo insuficiente.')
        else:
            self.saldo -= saque
            print(f'Você sacou {saque}! Seu saldo agora é de {self.saldo}')

    def mostrar_saldo(self):
        print(f'Seu saldo atual é {self.saldo}')


if __name__ == '__main__':
    conta = ContaBancaria('5548723', 500, 'Beatriz')
    print(conta.depositar())
    print(conta.sacar())
    print(conta.mostrar_saldo())
    



