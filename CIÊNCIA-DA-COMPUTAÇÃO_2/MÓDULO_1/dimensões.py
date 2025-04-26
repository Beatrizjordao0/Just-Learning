matriz =[[1,2,3,0],
         [4,5,6,3],
         [7,8,9,4]]


def dimensoes(matriz):
    lin = len(matriz)
    col = len(matriz[0])
    return f"{lin}X{col}"



print(dimensoes(matriz))