"""
    Faça um programa em Python que crie uma lista com os elementos
    10,15,20,25,30,35 depois remova o primeiro o segundo e o último elemento
    da lista.
"""

valores = [10, 15, 20, 25, 30, 35]

valores.pop(1)
valores.pop(0)
valores.pop()

print(valores)