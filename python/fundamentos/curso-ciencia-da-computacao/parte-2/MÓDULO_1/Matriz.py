def cria_matriz(nmr_linhas, nmr_colunas):
    matriz = [] # lista vazia
    for lin in range(nmr_linhas):
        linha = []
        for col in range(nmr_colunas):
            valor = int(input(f"Digite o número [{lin}][{col}]: "))
            linha.append(valor)

        matriz.append(linha)
    return matriz


def le_matriz():
    lin = int(input("Digite o número de linhas: "))
    col = int(input("Digite o número de colunas: "))
    return cria_matriz(lin, col)

matriz = le_matriz()



