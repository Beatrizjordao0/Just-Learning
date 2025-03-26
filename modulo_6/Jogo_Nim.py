
def computador_escolhe_jogada(n,m):
    if n % (m + 1) == 0: 
        return m
    else:
        jogada = n % (m + 1)
        if jogada > 0:
            return jogada
        else:
            return min(n, m)
        
# ----------------------------------------------------------------------------------------------------------   
#        
def usuario_escolhe_jogada (n,m):
    while True:
        pecas_tiradas = int(input("Quantas peças você vai tirar? \n"))
        
        if 1 <= pecas_tiradas <= m:
            return pecas_tiradas
            
        else:
            print("Oops! Jogada inválida! Tente de novo.\n")

# ----------------------------------------------------------------------------------------------------------  

def partida():
    print("Bem-vindo ao jogo do NIM! Escolha:\n")
    tipo_de_partida = input("1 - para jogar uma partida isolada \n"
"2 - para jogar um campeonato ")
    
# ---------------------------------------------------------------------------------------------------------- 
   
    if tipo_de_partida == '1':
        print("Você escolheu uma partida isolada!\n")

        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? \n"))
        if n < m:
            m = n
        ganhador = []
        vez_de_jogar = "N"
        jogada_J = 0
        jogada_C = 0
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////
        if n % (m + 1) == 0:
            print("Você começa!\n")
            vez_de_jogar = "J"
        else:
            print("Computador começa!\n")
            vez_de_jogar = "C"
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////
        while n > 0:
            if vez_de_jogar == "J":
                jogada_J = usuario_escolhe_jogada(n , m)
                n = n - jogada_J
                vez_de_jogar = "C"
                ganhador.append("J")

                if jogada_J == 1:
                    print("Você tirou uma peça.")
                else:
                    print("Você tirou",jogada_J,"peças.")

                if n == 1:
                    print("Agora resta apenas uma peça no tabuleiro.\n")
                else:
                    print("Agora restam",n,"peças no tabuleiro.\n")

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////
            else:
                jogada_C = computador_escolhe_jogada(n,m)
                n = n - jogada_C
                vez_de_jogar = "J"
                ganhador.append("C")

                if jogada_C == 1:
                    print("O computador tirou uma peça.")
                else:
                    print("O computador tirou",jogada_C,"peças.")

                if n == 1:
                    print("Agora resta apenas uma peça no tabuleiro.\n")
                else:
                    print("Agora restam",n,"peças no tabuleiro.\n")
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////
        placar = ganhador.pop()
        if placar == "C":
            print("Fim do jogo! O computador ganhou!")
        else:
            print("Fim do jogo! Você ganhou!")

# ----------------------------------------------------------------------------------------------------------  

    else:
        print("\nVocê escolheu um campeonato!\n")
        ganhador = [""]
        rodadas = 3
        rodada = 1
        pontos_J = 0
        pontos_C = 0
        while rodadas > 0:
            print("**** Rodada",rodada,"****\n")

            n = int(input("Quantas peças? "))
            m = int(input("Limite de peças por jogada? \n"))
            if n < m:
                m = n
            vez_de_jogar = "N"
            jogada_J = 0
            jogada_C = 0
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////
            if n % (m + 1) == 0:
                print("Você começa!\n")
                vez_de_jogar = "J"
            else:
                print("Computador começa!\n")
                vez_de_jogar = "C"
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////
            while n > 0:
                if vez_de_jogar == "J":
                    jogada_J = usuario_escolhe_jogada(n , m)
                    n = n - jogada_J
                    vez_de_jogar = "C"
                    ganhador.append("J")

                    if jogada_J == 1:
                        print("Você tirou uma peça.")
                    else:
                        print("Você tirou",jogada_J,"peças.")

                    if n == 1:
                        print("Agora resta apenas uma peça no tabuleiro.\n")
                    else:
                        print("Agora restam",n,"peças no tabuleiro.\n")

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////
                else:
                    jogada_C = computador_escolhe_jogada(n,m)
                    n = n - jogada_C
                    vez_de_jogar = "J"
                    ganhador.append("C")

                    if jogada_C == 1:
                        print("O computador tirou uma peça.")
                    else:
                        print("O computador tirou",jogada_C,"peças.")

                    if n == 1:
                        print("Agora resta apenas uma peça no tabuleiro.\n")
                    else:
                        print("Agora restam",n,"peças no tabuleiro.\n")
 # ////////////////////////////////////////////////////////////////////////////////////////////////////////////                       
            placar = ganhador.pop()
            if placar == "C":
                print("Fim do jogo! O computador ganhou!\n")
                pontos_C += 1
                rodada += 1
                rodadas -= 1
            else:
                print("Fim do jogo! Você ganhou!\n")
                pontos_J += 1
                rodada += 1
                rodadas -= 1
        print("**** Final do campeonato! ****\n")
        print("\nPlacar: Você",pontos_J,"X",pontos_C,"Computador")
                        


partida()
