"""
    Escreva um programa que recebe 4 valores e armazene em uma lista, 
    remova o primeiro e o último, mostre o tamanho da lista, 
    e diga se ela está vazia ou não.

"""

valores = []

for valor in range(4):
    v = int(input("Digite um valor: "))
    valores.append(v)
    print(valores)

ultimo = valores.pop()
print(valores)
primeiro = valores.pop(0)
print(valores)

print(len(valores))

if len(valores) == 0:
    print("A lista está vazia!")
elif len(valores) == 1:
    print("A lista tem apenas 1 valor")
else:
    print(f"A lista não está vazia! Ainda tem {len(valores)} valores")

