# dizer se um número é primo
#Números primos são divisíveis por ele mesmo ou por 1
print('Vamos descobrir se um número é primo ou não.')

numero = int(input('Digite um número: '))
divisiveis = 0
for i in range(1,numero + 1):
    if numero % i == 0:
        print('\033[32m', end='')
        divisiveis += 1
    else:
        print('\033[31m', end='')

    print(f'{i}', end='')
if divisiveis == 2:
    print(f'\n\033[35mO número {numero} é primo.')
else:
    print(f'\n\033[36mO número {numero} não é primo.')