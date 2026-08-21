class Livro:
    def __init__(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas
    
    def informacoes(self):
        return f"Título: {self.titulo}\nAutor: {self.autor}\nNúmero de Páginas: {self.num_paginas}"
    
    def calcular_palavras_por_pagina(self, num_palavras):
        if self.num_paginas > 0:
            return num_palavras / self.num_paginas
        else:
            return 0

# Exemplo de uso da classe Livro
livro1 = Livro("Bíblia", "Deus", 1500)

# Exibindo informações do livro
print(livro1.informacoes())

# Calculando a quantidade média de palavras por página (considerando um total de 50.000 palavras no livro)
palavras_totais = 10000
palavras_por_pagina = livro1.calcular_palavras_por_pagina(palavras_totais)
print(f"Palavras por página: {palavras_por_pagina:.2f}")
