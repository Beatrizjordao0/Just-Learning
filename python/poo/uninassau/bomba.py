class BombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro # 5 reais
        self.quantidadeCombustivel = 0

    def abastecerPorValor(self):
        print("Vamos abastecer seu carro por valor!\n")
        print("O valor do litro é: R$", self.valorLitro)
        valor = float(input("Digite quantos reais você quer colocar de combustível no seu carro: "))
        while True:
            if valor >= self.valorLitro:
                valor /= self.valorLitro # 20L
                self.quantidadeCombustivel += valor 
                print(f"A quantidade de Litros colocada foi: {valor}L")
                print(f"A quantidade de Litro no tanque é: {self.quantidadeCombustivel}L")
                break
            else:
                valor = float(input("Digite um valor válido: "))
            
    def abastecerPorLitro(self):
        print("Vamos abastecer seu carro por litro!\n")
        valor = float(input("Digite quantos litros você quer colocar no seu carro: "))
        Litro = valor # L
        valor *= self.valorLitro # R$
        self.quantidadeCombustivel += Litro
        print(f"O valor a ser pago é: R${valor}")
        print(f"A quantidade de Litro no tanque é: {self.quantidadeCombustivel}L")

    def alterarValor(self):
        self.valorLitro = float(input("Digite o novo valor do litro: "))

    def alterarCombustivel(self):
        self.tipoCombustivel = input("Digite o novo tipo de combustível: ")

    def alterarQuantidadeCombustivel(self):
        self.quantidadeCombustivel = float(input("Digite a nova quantidade de combustível: "))


if __name__ == "__main__":
    bomba = BombaCombustivel("Gasolina", 5)
    bomba.abastecerPorValor()
    bomba.abastecerPorLitro()
    bomba.alterarValor()













