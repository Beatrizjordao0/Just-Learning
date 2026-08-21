
class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    
    def perimetro(self):
        prmtr = 2 * self.altura + 2 * self.largura
        return prmtr
    
    def area(self):
        a = self.altura * self.largura
        return a

    
if __name__ == '__main__':
    retangulo = Retangulo(12, 15)


    print(f'A área do seu retângulo é {retangulo.area()}')

    print(f'O perímetro do seu retângulo é {retangulo.perimetro()}')