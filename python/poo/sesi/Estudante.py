
class Estudante:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.notas = []


    def adicionar_notas(self, notas):
        self.notas.append(notas)


    def media(self):
        soma = 0
        for nota in self.notas:
            soma += nota
        md = soma/len(self.notas)
        return md
    def aprovado(self):

        if Estudante.media(self) >= 6:
            print('Você foi aprovado!')
        else:
            print('Você foi reprovado!')


if __name__ == '__main__':
    estudante = Estudante('Beatriz', 16)

    nota1 = estudante.adicionar_notas(4)
    nota2 = estudante.adicionar_notas(5)
    print(estudante.media())
    print(estudante.aprovado())

