a = int(input("Qual vai ser o primeiro número do intervalo? "))
b = int(input("Qual vai ser o último número do intervalo? "))
pares = []
impares = []
for i in range(a, b + 1):
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print(f"Os números pares são:\n{pares}\nOs números ímpares são:\n{impares}")