'''
02/03/24
'''

numero = int(input('Digite um número que eu vou somar os dígitos dele.'))
soma = 0

while numero != 0:
    num = numero % 10
    soma += num
    numero = numero//10
   
print(soma)

