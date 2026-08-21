altura_max = float(input(f"Digite a 1º altura: "))
altura_min = 10000
for a in range(2, 16):
    altura = float(input(f"Digite a {a}º altura: "))
    if altura > altura_max:
        altura_max = altura
    if altura < altura_min:
        altura_min = altura
    

print(f"A altura máxima é: {altura_max}")
print(f"A altura mínima é: {altura_min}")