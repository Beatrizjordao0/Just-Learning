

class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def definir_nome(self, novo_nome):
        self.nome = novo_nome

    def definir_idade(self, nova_idade):
        self.idade = nova_idade

    def definir_altura(self, nova_altura):
        self.altura = nova_altura

    def obter_nome(self):
        return self.nome

    def obter_idade(self):
        return self.idade

    def obter_altura(self):
        return self.altura

    def cumprimentar(self):
        return f"Olá, meu nome é {self.nome}. Prazer em conhecê-lo!"

# Exemplo de uso da classe Pessoa
if __name__ == "__main__":
    # Criando uma pessoa
    pessoa1 = Pessoa("João", 30, 1.75)

    # Obtendo informações da pessoa
    print(f"Nome: {pessoa1.obter_nome()}")
    print(f"Idade: {pessoa1.obter_idade()} anos")
    print(f"Altura: {pessoa1.obter_altura()} metros")

    # Cumprimentando a pessoa
    print(pessoa1.cumprimentar())

    # Alterando informações da pessoa
    pessoa1.definir_nome("Maria")
    pessoa1.definir_idade(25)
    pessoa1.definir_altura(1.68)

    # Obtendo novas informações da pessoa
    print(f"Novo nome: {pessoa1.obter_nome()}")
    print(f"Nova idade: {pessoa1.obter_idade()} anos")
    print(f"Nova altura: {pessoa1.obter_altura()} metros")
    print(pessoa1.cumprimentar())
