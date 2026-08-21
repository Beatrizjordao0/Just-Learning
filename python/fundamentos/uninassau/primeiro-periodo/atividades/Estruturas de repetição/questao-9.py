n = int(input("Digite um número para saber o seu fatorial: "))

a = n
for numero in range(n-1, 0, -1):
    c = a * numero
    a = c
print(a)