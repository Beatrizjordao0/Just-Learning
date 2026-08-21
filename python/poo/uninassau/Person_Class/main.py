
class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        for ano in range(anos):
            if self.idade < 21:
                self.altura += 0.5
                self.idade += 1
                print(f"Sua idade agora é: {self.idade}\n"
                      f"Sua altura é: {self.altura}")
            else:
                self.idade += 1
                print(f"Sua idade agora é: {self.idade}")

    
    def engordar(self, kilo):
        self.peso += kilo
        

    def emagrecer(self, kilo):
        self.peso -= kilo
       

    def crescer(self, cm):
        self.altura += cm
        
    
    def __str__(self):
        return (f"Nome: {self.nome}\n"
                f"Idade: {self.idade}\n"
                f"Peso: {self.peso:.1f} kg\n"
                f"Altura: {self.altura:.1f} cm\n")



if __name__ == "__main__":
    nome = input("Digite o seu nome: ")
    idade = int(input("Digite a sua idade: "))
    peso = float(input("Digite o seu peso em kg: "))
    altura = int(input("Digite a sua altura em cm: "))


    pessoa = Pessoa(nome, idade, peso, altura)

    continuar = True

    while continuar:
        print("Digite 1-Envelhecer, 2-engordar, 3-emagrecer, 4-crescer, 5-sair: ")
        escolha = input("")

        if escolha == "5":
            print("Bye Bye \n")
            continuar = False
        elif escolha =="4":
            cm = int(input("Digite quantos centímetros: "))
            pessoa.crescer(cm)
        elif escolha =="3":
            kilo = float(input("Digite quantos kilos vai emagrecer: "))
            pessoa.emagrecer(kilo)
        elif escolha == "2":
            kilo = float(input("Digite quantos kilos vai engordar: "))
            pessoa.engordar(kilo)
        elif escolha == "1":
            anos = int(input("Digite quantos anos vai envelhecer: "))
            pessoa.envelhecer(anos)
        else:
            print("Por favor digite um valor válido!")
            escolha = input("Digite 1-Envelhecer, 2-engordar, 3-emagrecer, 4-crescer, 5-sair: ")

    print("Seus dados ficaram assim:")
    print(pessoa)


    
    
    
    
    




