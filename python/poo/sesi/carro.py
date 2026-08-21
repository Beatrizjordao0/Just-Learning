
class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def ligar(self):
        print(f'O seu carro {self.modelo} de cor {self.cor} ligou.')

    def desligar(self):
        print(f'O seu carro de modelo {self.modelo} da marca {self.marca} desligou')

    def acelerar(self):
        print(f'O Seu carro está acelerando!!!')




if __name__ == '__main__':
    carro1 = Carro('BMW', 'i8', '2015', 'branco')
    print(carro1.ligar())
