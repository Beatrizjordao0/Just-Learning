'''Desafio: Criar uma calculadora que receba x números e opere com uma operação todas elas'''

#passo a passo:
#   Passo 1: Definir quantos números eu quero operar
#   Passo 2: formar as 4 operações: Divisão, Multiplicação, Subtração, Adição
#   Passo 3: Aplicar e mostrar ao usuário a resposta da operação entre os x números
import time
import Módulo_operações
from colorama import Fore, Style
#-----------------------------------------------------------------------------------
texto = (f'Digite {Fore.RED}soma {Style.RESET_ALL}para somar, {Fore.YELLOW}subtração {Style.RESET_ALL}'
         f'para subtrair, {Fore.GREEN}divisão {Style.RESET_ALL}para dividir ou {Fore.BLUE}multiplicação'
         f'{Style.RESET_ALL} para multiplicar.')
#---------------------------------------------------------------------------------


print('Olá!! Bem vindo(a) à minha calculadora em python!\n'
      'Você escolhe quantos números você quer somar, subtrair, dividir ou multiplicar!\n')
print(texto)
print('lembre se de escrever do jeito que eu lhe digo para fazer. Se tentares fazer algo diferente,'
      'vai dar ERRO.'
      'Boa sorte.')

while True:
    qntd = Módulo_operações.quantidade()
    operacao = input('Digite aqui a operação que você quer fazer, ou digite S para sair\n')
    if operacao == 'soma' or operacao == 'Soma':
        soma = Módulo_operações.adicao(qntd)
        print(f'{Fore.YELLOW}A soma dos números é: {soma}{Style.RESET_ALL}')

    elif operacao == 'subtração' or operacao == 'Subtração':
        subtracao = Módulo_operações.subtracao(qntd)
        print(f'{Fore.RED}A subtração dos números é: {subtracao}{Style.RESET_ALL}')

    elif operacao == 'multiplicação' or operacao == 'Multiplicação':
        multiplicação = Módulo_operações.multiplicacao(qntd)
        print(f'{Fore.GREEN}A multiplicação entre os números é: {multiplicação}{Style.RESET_ALL}')

    elif operacao == 'Divisão' or operacao == 'divisão':
        divisao = Módulo_operações.divisao(qntd)
        print(f'{Fore.BLUE}A divisão entre os números é: {divisao}{Style.RESET_ALL}')

    elif operacao == 'S' or operacao == 's':
        print('Você sairá em 3 segundos:')
        time.sleep(1)
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)
        break

    else:
        operacao = input('Parece que você digitou algo errado :(\n'
                         'Tente novamente: ')