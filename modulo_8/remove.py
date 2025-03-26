lista = [1, 2, 3, 5, 6, 7, 6, 5, 8, 9, 3, 9, 5, 7, 0, 1, 3, 5, 0, 5, 6, 7, 4, 4]

def remove_repetidos(lista):
    lista = list(set(lista))
    lista.sort()
    return lista

print(remove_repetidos(lista))