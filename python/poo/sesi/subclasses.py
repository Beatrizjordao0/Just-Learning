
class Veiculo():
    def __init__(self, marca, modelo, nome):
        self.marca = marca
        self.modelo = modelo
        self.nome = nome

    def frear(self):
        print(f'O {self.nome} freou!')

    def acelerar(self):
        print(f'O {self.nome} acelerou!')

class Carro(Veiculo):
    def __init__(self,marca, modelo, cor):
        super().__init__(marca, modelo, 'carro')   # Usamos o super().__init__(parâmetros) para mostrar que herdamos atributos do pai
        self.cor = cor

    def abrir_porta(self):
        print('A porta abriu')


class Moto(Veiculo):
    def __init__(self,marca, modelo, cilindrada):
        super().__init__(marca, modelo, 'moto')  # A mesma coisa acontece aqui. A classe moto está herdando atributos de Veículo, seu pai
        self.cilindrada = cilindrada

if __name__ == '__main__':
    carro = Carro('BMW','X6','Azul cromado')
    moto = Moto('Honda','CBR',25)

    print(carro.acelerar())
    print(moto.frear())
    print(carro.abrir_porta())
    print(moto.acelerar())
    print(moto.marca)
    print(carro.modelo)
