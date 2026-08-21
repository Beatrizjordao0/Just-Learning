
# Atividade 5 - Revisão de listas

palavras = ["casa", "bola", "arvore", "carro", "avião", "bicicleta"]

print(palavras)

nova_lista = []

for p in palavras:
    if len(p) > 4:
        nova_lista.append(p)

print(nova_lista)

nova_lista.reverse()
maiuscula = []

for p in nova_lista:
    maiuscula.append(p.upper())

print(maiuscula)    