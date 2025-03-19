largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

for a in range(altura):
    for l in range(largura):
        if a == 0 or a == altura - 1 or l == 0 or l == largura - 1:
            print("#", end='')
        else:
            print(" ", end='')
    print()

