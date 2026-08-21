"""
Crie um programa que define uma classe pessoa, 
com nome, idade e data de nascimento.
Ainda neste programa crie uma outra classe, 
aluno, que herde a classe pessoa, e além disso tenha um atributo matrícula. 
Na execução do programa o usuário deve preencher todas as informações de um
funcionário.

"""
class Pessoa:
    def __init__(self):
        self.nome = input("Digite seu nome: ") 
        self.idade = int(input("Digite sua idade: "))
        self.data_nasc = input("Digite sua data de nascimento: ")

class Aluno(Pessoa): 
    def __init__(self):
        Pessoa.__init__(self)
        self.matricula = int(input("Digite sua matrícula: "))
        
    def mostrar_info(self):
        print(f"Nome: {self.nome}\n"
              f"Idade: {self.idade}\n"
              f"Data de Nascimento: {self.data_nasc}\n"
              f"Matrícula: {self.matricula}\n")


aluno = Aluno()

aluno.mostrar_info()




