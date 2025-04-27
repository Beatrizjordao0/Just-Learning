
m1 = [[1,2,3],
      [4,5,6],
      [7,8,9]]

m2 = [[1,5,7],
      [3,5,4],
      [4,8,5]]
#////////////////////////////////////////////////////////////////////////////////////////
def dimensoes(matriz):
    lin = len(matriz)
    col = len(matriz[0])
    
    return f"{lin}X{col}"

#///////////////////////////////////////////////////////////////////////////////////////

def soma_matrizes(m1, m2):
    if dimensoes(m1) != dimensoes(m2):
        return False
    
    soma = []
    for i in range(len(m1)):
        linha = []
        for j in range(len(m1[0])):
            linha.append(m1[i][j] + m2[i][j])
        soma.append(linha)
    
    return soma


print(soma_matrizes(m1, m2))