"""
Crie uma classe simples em Python para representar um carro. 
O carro terá alguns atributos, como modelo, ano e velocidade, 
e métodos para acelerar e imprimir as informações do carro. 
"""

class Carro:
    # Construtor da classe
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0
        
    # Método para acelerar o carro
    def acelerar(self, incremento):
        self.velocidade += incremento
        print(f"O carro acelerou {incremento} km/h. Velocidade atual: {self.velocidade} km/h\n")
    
    # Método para imprimir as informações do carro
    def imprimir_informacoes(self):
        print(f"Modelo: {self.modelo},\n" 
              f"Ano: {self.ano}, \n"
              f"Velocidade: {self.velocidade} km/h \n")

# Exemplo de uso
meu_carro = Carro("Toyota Corolla", 2020)
meu_carro.acelerar(20)
meu_carro.imprimir_informacoes()

meu_carro.acelerar(30)
meu_carro.imprimir_informacoes()
