
import random

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def atualizar(self):
        NovoCarregamento = random.randint(20,500)
        print(f'Chegou um novo carregamento de produtos! foram {NovoCarregamento} novos produtos.')
        self.quantidade += NovoCarregamento
        print(f'Agora você tem {int(self.quantidade)} produtos totais.')

    def PrecoTotal(self):
        precototal = int(self.quantidade) * int(self.preco)
        return int(precototal)
    
    def quant(self):
        return self.quantidade


if __name__ == '__main__':
    cafe = Produto('Café', 2, 20)
    print(f'Você tem {cafe.quant()} cafés no seu estoque.\n O valor total é de {cafe.PrecoTotal()}')
    print(cafe.atualizar())
    print(f'Você tem {cafe.quant()} cafés')
    print(f'Após o carregamento, o valor total do estoque é de {cafe.PrecoTotal()}')