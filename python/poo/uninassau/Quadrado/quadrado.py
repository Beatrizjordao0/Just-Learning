"""
    Crie um programa que defina uma classe quadrado, 
    que tenha como atributo o lado, 
    receba essa informação do usuário, 
    a classe também deve conter um método
      para calcular e mostrar a área do quadrado, dada por lado*lado.

"""
class Quadrado: 
    def __init__(self):
        self.lado = int(input("digite o valor do lado: "))
        self.area = 1

    def calculo_area(self):
        self.area = self.lado * self.lado

        print("A sua area é:", self.area)


if __name__ == "__main__":
    quadrado = Quadrado()
    quadrado.calculo_area()
