#Meu joguinho de dinheiro

print('\033[35m                 |------     | JOGO DO CAPITALISTA |     ------|\033[0m\n\n\n\n')


#----------------------------------------------------------------------------------------------------------------------------------
import time
import random
#----------------------------------------------------------------------------------------------------------------------------------

dinheiro_banco = 500
dinheiro_comigo = 150
rodada = 1
escolha_por_rodada = []

#----------------------------------------------------------------------------------------------------------------------------------
#   REGRAS

print('\033[40;1;36mOlá Jogador. Leia atentamente tudo o que estiver abaixo!\033[0m\n\n\n')
print('\033[0;1;35m1º Você pode sacar dinheiro do banco.\n')
print('\033[0;1;35m         Se você sacar o dinheiro você pode investir uma quantia na bolsa de valores.\n')
print('\033[0;1;35m         Se der certo você dobra o valor, se der errado você perde o valor investido.')
print('\033[0;1;32m2º Você deve continuar depositando dinheiro no banco!\n')
print('\033[0;1;31m         Se demorar demais para depositar dinheiro no banco o ladrão vai roubar você!\n')
print('\033[0;1;31m         O ladrão vai roubar entre 20 e 200 coins, então cuidado!\n')
print('\033[0;1;32m3º Para ganhar dinheiro você pode trabalhar!\n')
print('\033[0;1;32m         Você pode ganhar de 20 a 250 coins no trabalho.\n')
print('\033[0;1;33m4º O ladrão pode te roubar ou não a cada tres rodadas.\n')
print('\033[0;1;34m         Se mesmo assim você não depositar na próxima rodada o ladrão rouba o dobro do máximo possível que é 100.\033[0m\n')
print('\033[40;1;31m5º O dinheiro que você vai ganhar no trabalho vai depender do seu rendimento no mesmo.\033[0m\n')
print('\033[0;1;31m         péssimo = 20 coins')
print('\033[0;1;31m         ruim = 50 coins')
print('\033[0;1;33m         bom = 100 coins')
print('\033[0;1;32m         ótimo = 150 coins')
print('\033[0;1;36m         excelente = 250 coins\033[0m\n')

nome = input('Para começar deixe-me saber seu nome: -> ')
print(f'\nSaldo com você é \033[33m{dinheiro_comigo}\033[0m coins')
print(f'\nSaldo no banco é \033[33m{dinheiro_banco}\033[0m coins\n')



def trabalho():
    global dinheiro_comigo
    global escolha_por_rodada
    
    print('Você saiu de casa para seu emprego.')
    time.sleep(2)
    print('Você chegou no trabalho!')
    print('Você trabalha por 5 segundos.')
    time.sleep(5)
    rendimento = ['\033[31mpéssimo','\033[31mruim','\033[33mbom','\033[32mótimo','\033[36mexcelente\033[0m']
    rendimento = random.choice(rendimento)
    print(f'Seu rendimento foi {rendimento}')
    print('Vamos adicionar na sua conta já!!')
    if rendimento == 'péssimo':
        ganho = 20
        dinheiro_comigo += ganho
    elif rendimento == 'ruim':
        ganho = 50
        dinheiro_comigo += ganho
    elif rendimento == 'bom':
        ganho = 100
        dinheiro_comigo += ganho
    elif rendimento == 'ótimo':
        ganho = 150
        dinheiro_comigo += ganho
    else:
        ganho = 250
        dinheiro_comigo += ganho
    print(f'Seu saldo atual é de \033[32m{dinheiro_comigo}\033[0m coins')
    escolha_por_rodada.append('trabalho')

def sacar():
    global dinheiro_banco
    global dinheiro_comigo
    global escolha_por_rodada
    while True:
        quantia = int(input('Quantos coins você quer sacar? -> '))
        if quantia <= dinheiro_banco:
            dinheiro_banco -= quantia
            dinheiro_comigo += quantia
            time.sleep(1)
            print(f'Seu saldo no banco agora é de \033[32m{dinheiro_banco}\033[0m.')
            time.sleep(1)
            print(f'Você acabou de sacar. Seu bolso tem \033[33m{dinheiro_comigo}\033[0m coins')
            break
        else:
            print('\033[31m SALDO INSUFICIENTE!\033[0m') 
            print(f'Seu saldo é de \033[33m{dinheiro_banco}\033[0m coins.')
    escolha_por_rodada.append('saque')


def depositar():
    global dinheiro_banco
    global dinheiro_comigo
    global escolha_por_rodada
    while True:
        quantia = int(input('Quantos coins você quer depositar? -> '))
        if quantia > dinheiro_comigo:
            print('\033[31m SALDO INSUFICIENTE!\033[0m')
            print(f'No seu bolso tem \033[32m{dinheiro_comigo}\033[0m coins')
        else:
            dinheiro_comigo -= quantia
            dinheiro_banco += quantia
            time.sleep(1)
            print(f'Seu bolso agora tem \033[32m{dinheiro_comigo}\033[0m coins')
            print(f'O seu banco agora tem \033[32m{dinheiro_banco}\033[0m coins')
            break
    escolha_por_rodada.append('depositar')



def investir():
    global dinheiro_banco
    global dinheiro_comigo
    global escolha_por_rodada

    while True:
        bolsa = ['perdeu','ganhou','ganhou','perdeu','ganhou']
        bolsa1 = random.choice(bolsa)
    
        quantia = int(input('Quantos coins você quer investir? -> '))
        print(f'O resultado da bolsa foi: \033[32m{bolsa1}\033[0m')
        dinheiro_comigo -= quantia

        if quantia > dinheiro_comigo:
            print('\033[31m SALDO INSUFICIENTE!\033[0m')
            print(f'No seu bolso tem {dinheiro_comigo} coins\n')

        else:
            if bolsa1 =='ganhou':
                quantia *= 2
                print(f'Você ganhou \033[32m{quantia}\033[0m coins')
                dinheiro_comigo += quantia
                print(f'Seu saldo atual é de \033[32m{dinheiro_comigo}\033[0m coins\n')
                break

            else:
                print('Você perdeu tudo.')
                print(f'Seu saldo atual é de {dinheiro_comigo}\033[0m coins\n')
                break

    escolha_por_rodada.append('investir')



def ladrao():
    global escolha_por_rodada
    global dinheiro_banco
    
    if 'depositar' in escolha_por_rodada[:3]:
        print('Um ladrão foi visto tentando roubar o banco, mas ele não conseguiu.\n')
        escolha_por_rodada.clear() 
    else: 
        quantia = random.randint(20,200)
        print(f'O ladrão roubou seu banco!! Ele levou \033[31m{quantia}\033[0m coins\n')
        dinheiro_banco -= quantia
        print(f'Seu saldo do banco agora é \033[33m{dinheiro_banco}\033[0m coins.\n')



contador = 0
while True:
    contador += 1 
    print(f'Rodada \033[36m{contador}\033[0m')
    print(f'Suas escolhas de rodadas foram {escolha_por_rodada}')

    ação = input('Qual ação você deseja fazer? ou digite sair para sair. -> ')

    if ação == 'trabalhar':
        trabalho()
    elif ação == 'depositar':
        depositar()
    elif ação == 'investir':
        investir()
    elif ação == 'sacar':
        sacar()
    elif ação == 'sair':
        break
    elif dinheiro_banco == 0 and dinheiro_comigo == 0:
        print('PERDEU!')
        break
    else:
        print('Escreva algo válido.')

    vai_roubar = ['sim','não']
    vai_roubar1 = random.choice(vai_roubar)
    
    if contador % 3 == 0:
        print(f'Será que o ladrão vai roubar? {vai_roubar1}')
        if vai_roubar1 == 'sim':
            ladrao()
            

 