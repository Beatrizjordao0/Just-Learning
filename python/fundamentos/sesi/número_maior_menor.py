def teste(num1, num2):
    if num1 > num2:
        print(f'{num1} é maior do que {num2}')
    elif num1 < num2:
        print(f'{num2} é maior que o número {num1}')
    else:
        print('Os números são iguais')


numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))

teste(numero1, numero2)
