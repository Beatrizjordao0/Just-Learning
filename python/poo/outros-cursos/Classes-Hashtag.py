# OPP
km = 1
class Pessoa:
    def __init__(self, nome, cpf, sexo):
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf

if __name__=='__main__':
    pessoa1 = Pessoa('bia', '16646401433', 'F')
    pessoa2 = Pessoa('Carlos', '44448881898', 'M')


class Carro:
    # Atributos
    def __init__(self, modelo, placa, ano):
        self.modelo = modelo
        self.placa = placa
        self.ano = ano

    # Métodos
    def andar():
        km_andados = int(input('Quantos km você quer andar com o carro?'))
        km = km * km_andados
        if km == 0:
            print('Você não saiu do lugar.')
        elif km < 0:
            print(f'Você andou para trás.')
        else:
            print(f'Você andou {km} kilômetros')


    

if __name__ == '__main__':
    palio = Carro('palio', 'BNKL-5843', '2015')

    palio.andar

        
    
    

    
