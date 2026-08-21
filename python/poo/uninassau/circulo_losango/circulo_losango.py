class circulo:
    def __init__(self, raio, area):
        self.raio = raio
        self.area = area

    def calcular_area(self):
        self.area = 3.141 * (self.raio ** 2)
        print(f"A área do círculo é: {self.area}")
    
class losango:
    def __init__(self, altura, largura, area):
        self.altura = altura
        self.largura = largura
        self.area = area

    def calcular_area(self):
        self.area = self.altura * self.largura 
        print(f"A área do losango é: {self.area}")

    def __del__(self):
        print("Objeto losango deletado")


if __name__ == "__main__":
    circulo1 = circulo(5, 0)
    circulo1.calcular_area()

    losango1 = losango(4, 6, 0)
    losango1.calcular_area()
    del losango1
        