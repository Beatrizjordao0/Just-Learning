'''Arquivo auxiliar do arquivo principal2.py'''

#Desafio: Calculadora que receba vários valores e devolva 4 operações.

# Passo 1: Definir quantos números eu quero operar.
# receber a quantidade de números
#armazenar os números em uma variável lista
def quantidade():
    numeros = []
    quantos = int(input('Quantos números você quer operar?: '))
    for i in range(quantos):
        numero = float(input(f'Digite o {i+1}º número: '))
        numeros.append(numero)

    return numeros
#armazenei os numeros na função quantidade para fins futuros

def adicao(x):
    soma = sum(x)
    return soma

def subtracao(x):
    subtrair = x[0] - sum(x[1:])
    return subtrair

def multiplicacao(x):
    multiplicar = 1
    for i in x:
        multiplicar = multiplicar * i
    return multiplicar

def divisao(x):
    dividir = x[0]
    for i in x[1:]:
        if i == 0:
            return 'Erro! não da pra dividir por 0 né querido. '
        elif i != 0:
            dividir = dividir/i
    return dividir



