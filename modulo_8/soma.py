lista = [1, 2, 3, 5, 6, 7, 6.8, 5, 8.3, 9, 3, 9, 5, 7, 0, 1, 3, 5, 0, 5, 6, 7, 4, 4]

def soma_elementos(lista):
    s = 0
    for i in lista:
        s += i
    return s



print(soma_elementos(lista))

