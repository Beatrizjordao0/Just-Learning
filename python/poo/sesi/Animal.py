
class Animal:
    def __init__(self, nome, idade, especie):
        self.nome = nome
        self.idade = idade
        self.especie = especie

    def emitir_som(self):
        if self.especie == 'gato':
            print('Miau')
        elif self.especie == 'cachorro':
            print('Roof Roof')
        elif self.especie == 'passaro':
            print('piu piu')
        else:
            print(f'O {self.nome} emitiu o som de {self.especie}')

if __name__ == '__main__':
    gato = Animal('Oliver', '6 meses', 'gato')
    cachorro = Animal('Nina', '2 anos', 'cachorro')

    print(gato.emitir_som())
    print(f'Informações do cachorro:\n nome:',cachorro.nome,'\n idade:',cachorro.idade,'\n espécie:',cachorro.especie)