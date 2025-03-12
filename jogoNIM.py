"""Você deverá escrever um programa na linguagem Python, versão 3, 
que permita a uma "vítima" jogar o NIM contra o computador. 
O computador, é claro, deverá seguir a estratégia vencedora descrita acima.

Sejam n o número de peças inicial e m o número máximo de peças 
que é possível retirar em uma rodada. 
Para garantir que o computador ganhe sempre, 
é preciso considerar os dois cenários possíveis para o início do jogo:

Se n é múltiplo de (m+1), o computador deve ser "generoso" 
e convidar o jogador a iniciar a partida com a frase "Você começa!"

Caso contrário, o computador toma a iniciativa de começar o jogo, 
declarando "Computador começa!"

Uma vez iniciado o jogo, a estratégia do computador para ganhar 
consiste em deixar sempre um número de peças que seja 
múltiplo de (m+1) ao jogador. Caso isso não seja possível, 
deverá tirar o número máximo de peças possíveis.

Seu trabalho, então, será implementar o Jogo e fazer com que o 
computador se utilize da estratégia vencedora."""

"""
n = peças inicias

m = peças que podem ser retiradas por jogada"""

def usuario_escolhe_jogada(n, m):
    while True:
        pecas_tiradas = int(input("Quantas peças você vai tirar? "))
        
        if 1 <= pecas_tiradas <= m:
            return pecas_tiradas
            
        else:
            print("Oops! Jogada inválida! Tente de novo.")


def computador_escolhe_jogada(n, m):
    if n % (m + 1) == 0: 
        return m
    else:
        jogada = n % (m + 1)
        if jogada > 0:
            return jogada
        else:
            return min(n, m)

        

def partida(tipo):
    Vez_de_Jogar = 0
    if tipo == "1":
        print("Voce escolheu uma partida isolada!\n")
        partida_isolada(Vez_de_Jogar)
        
    elif tipo == "2":
        print("Voce escolheu um campeonato!")
        campeonato(Vez_de_Jogar)


def partida_isolada(vez_de_jogar):
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? \n"))

    if n % (m + 1) == 0:
        print("Voce começa!\n")
        vez_de_Jogar = "Jogador"

    elif n % (m + 1) != 0:
        print("Computador começa!\n")
        vez_de_Jogar = "Computador"

    vezes_jogadas = []
    jogador = []
    while n >= 1:

        if vez_de_Jogar == "Jogador":
            jogador = "Jogador"
            jogada = usuario_escolhe_jogada(n, m)
            n = n - jogada
            if jogada == 1:
                print("Você tirou uma peça.")
            else:
                print("Você tirou",jogada,"peças.")

            if n == 1:
                print("Agora resta apenas uma peça no tabuleiro.\n")
            else:
                print("Agora restam",n,"peças no tabuleiro.\n")
            vez_de_Jogar = "Computador"
            vezes_jogadas.append(jogador)
    

        else:
            jogador = "Computador"
            jogada = computador_escolhe_jogada(n,m)
            n = n - jogada
            if jogada == 1:
                print("O computador tirou uma peça.")
            else:
                print("O computador tirou",jogada,"peças.")

            if n == 1:
                print("Agora resta apenas uma peça no tabuleiro.\n")
            else:
                print("Agora restam",n,"peças no tabuleiro.\n")
            vez_de_Jogar = "Jogador"
            vezes_jogadas.append(jogador)
    placar = vezes_jogadas.pop()

    if placar == "Jogador":
        print("Fim de jogo! Você ganhou!")
    else:
        print("Fim do jogo! O computador ganhou!")
            

def campeonato(n,m):
    partidas = 3

def main():
    n = 0
    m = 0
    print('Bem-vindo ao jogo do NIM! Escolha:')
    tipoDePartida = input("1 - para jogar uma partida isolada \n"
    "2 - para jogar um campeonato ")

    partida(tipoDePartida)




main()


