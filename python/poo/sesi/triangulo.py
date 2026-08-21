
class Triangulo:
    def __init__(self,lado1, lado2, base):
        # Atributos
        self.lado1 = lado1
        self.lado2 = lado2
        self.base = base

    # Métodos
    def área(self):
        altura = int(input(f'Qual a altura do triângulo de base {self.base}?'))
        area = self.base * altura / 2
        return area
    
    def perimetro(self):
        soma_dos_lados = self.lado1 + self.base + self.lado2
        return soma_dos_lados
    

if __name__ == '__main__':
    triangulo = Triangulo(3,4,6)
    print(f'O valor da área do seu triangulo é {triangulo.área()}\n')
    print(f'O perímetro do seu triangulo é {triangulo.perimetro()}')
    

    
        