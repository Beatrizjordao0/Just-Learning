import geometria as gm

nomes = []
nome = input("Digite um nome para ser sorteado: ")
nomes.append(nome)
while nome:
    nome = input("Digite outro nome para ser sorteado: (aperte enter para sair) ")
    nomes.append(nome)

ganhadores = gm.sorteio_ganhadores(nomes)

print(f"Os 3 ganhadores são: {ganhadores}.")