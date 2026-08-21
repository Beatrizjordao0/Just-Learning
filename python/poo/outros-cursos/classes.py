# Quando falamos de OOP,
# estamos nos referindo a um conjunto de conceitos e padrões
# que usamos para resolver problemas com objetos.

# Um objeto em Python é uma única coleção de dados (atributos) e comportamento (métodos).
# Você pode pensar em objetos como coisas reais ao seu redor.

'''
# Uma calculadora pode ser um objeto:
# Atributos --> cor, tamanho, botões
# Métodos --> soma, divisão, multiplicação e subtração
'''

# Como você pode notar, os dados (atributos) são sempre substantivos,
# enquanto os comportamentos (método) são sempre verbos.


class Cookie:
    # constructor
    def __init__(self, size, shape, name, taste, chips = 'chocolate'):
        # instance attributes
        self.size = size
        self.shape = shape
        self.name = name
        self.taste = taste
        self.chips = chips
    # The object is passing itself as a parameter
    # It is going to bake the Cookie
    def bake(self):
        print(f'This {self.name} is being baked with the shape {self.shape} and it\'s taste is {self.taste} with {self.chips} chips')
        print('Your cookie is already ready!')
    

cookie1 = Cookie(2, 'circle', 'Woman', 'vanilla')

print(cookie1.bake())

# print(id(cookie1))