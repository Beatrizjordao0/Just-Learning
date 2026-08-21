import random

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
        
def usuario_escolhe_jogada (n,m):
    while True:
        pecas_tiradas = int(input("Quantas peças você vai tirar? "))
        
        if 1 <= pecas_tiradas <= m:
            return pecas_tiradas
            
        else:
            print("Oops! Jogada inválida! Tente de novo.\n")

# ----------------------------------------------------------------------------------------------------------  

def partida():
    print("Bem-vindo ao jogo do NIM!\n\nAfinal, o que é o jogo do Nim e como jogar?")
    print("""
        ***** CONFIGURAÇÕES *****
          
        Você escolherá quantas peças
        terão no tabuleiro e quantas
        peças poderão ser tiradas 
        por cada vez.
          
        ***** COMEÇANDO *****
          
        Você só poderá tirar a
        quantidade de peças
        acordadas anteriormente.
          
        Quem conseguir tirar a últi-
        ma peça ganha.
          
        Boa sorte!!
          
        Agora escolha: 
         """)
    tipo_de_partida = input("1 - Para jogar uma partida isolada \n"
"2 - Para jogar um campeonato\n3 - Partida Multijogador --> ")
    
# ---------------------------------------------------------------------------------------------------------- 
   
    if tipo_de_partida == '1':
        print("Você escolheu uma partida isolada!\n")

        n = int(input("Quantas peças terá no tabuleiro? "))
        m = int(input("Limite de peças por jogada? \n"))
        if n < m:
            m = n
        ganhador = []
        vez_de_jogar = "N"
        jogada_J = 0
        jogada_C = 0
        jogadas = ["J", "C"]
        jogada = random.choice(jogadas)
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////
        if jogada == "J":
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

    elif tipo_de_partida == "2":
        print("\nVocê escolheu um campeonato!\n")
        ganhador = [""]
        rodadas = 3
        rodada = 1
        pontos_J = 0
        pontos_C = 0
        while rodadas > 0:
            print("**** Rodada",rodada,"****\n")

            n = int(input("Quantas peças terá no tabuleiro? "))
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
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////                       
                          
    elif tipo_de_partida == "3":
        print("Você escolheu a partida Multijogador!!\n\n" \
        "Aqui será você contra o seu amigo.\n\n" \
        "Comecem inserindo seus nomes: \n\n")

        nome_jogador_1 = input("Digite o nome do Jogador 1: ")
        nome_jogador_2 = input("Digite o nome do Jogador 2: ")

        print(f"Olá {nome_jogador_1} e {nome_jogador_2}! Agora que estamos aqui " \
              "vou lhes explicar como funciona o jogo.")
        
        print("""
        ***** CONFIGURAÇÕES *****
          
        Você escolherá quantas peças
        terão no tabuleiro e quantas
        peças poderão ser tiradas 
        por cada vez.
          
        ***** COMEÇANDO *****
          
        Você só poderá tirar a
        quantidade de peças
        acordadas anteriormente.
          
        Quem conseguir tirar a últi-
        ma peça ganha.
          
        Boa sorte!!
              
        Desejam jogar campeonato ou partida isolada?
        """)
        
        tipo_de_partida = input("1 - Para jogar uma partida isolada \n"
                                "2 - Para jogar um campeonato\n\n")
        
        if tipo_de_partida == "1":
            print("Vocês escolheram uma partida isolada! \n")

            n = int(input("Quantas peças terá no tabuleiro? "))
            m = int(input("Limite de peças por jogada? "))
            if n < m:
                m = n
            ganhador = []
            vez_de_jogar = "N"
            jogada_1 = 0
            jogada_2 = 0
            jogadas = ["1", "2"]
            jogada = random.choice(jogadas)
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////
            if jogada == "1":
                print(f"{nome_jogador_1} começa!\n")
                vez_de_jogar = "1"
            else:
                print(f"{nome_jogador_2} começa!\n")
                vez_de_jogar = "2"

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////
            while n > 0:
                if vez_de_jogar == "1":
                    print(f"Vez de {nome_jogador_1}\n\n")
                    jogada_1 = usuario_escolhe_jogada(n , m)
                    n = n - jogada_1
                    vez_de_jogar = "2"
                    ganhador.append("1")

                    if jogada_1 == 1:
                        print(f"{nome_jogador_1} tirou uma peça.\n")
                    else:
                        print(f"{nome_jogador_1} tirou",jogada_1,"peças.\n")

                    if n == 1:
                        print("Agora resta apenas uma peça no tabuleiro.\n")
                    else:
                        print("Agora restam",n,"peças no tabuleiro.\n")    

                elif vez_de_jogar == "2":
                    print(f"Vez de {nome_jogador_2}\n\n")
                    jogada_2 = usuario_escolhe_jogada(n , m)
                    n = n - jogada_2
                    vez_de_jogar = "1"
                    ganhador.append("2")

                    if jogada_2 == 1:
                        print(f"{nome_jogador_2} tirou uma peça.\n")
                    else:
                        print(f"{nome_jogador_2} tirou",jogada_2,"peças.\n")

                    if n == 1:
                        print("Agora resta apenas uma peça no tabuleiro.\n")
                    else:
                        print("Agora restam",n,"peças no tabuleiro.\n")

            placar = ganhador.pop()
            if placar == "1":
                print(f"Fim do jogo! {nome_jogador_1} ganhou!")
            else:
                print(f"Fim do jogo! {nome_jogador_2} ganhou!")

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////            
        
        elif tipo_de_partida == "2":
            print("\nVocês escolheram um campeonato!\n")
            ganhador = [""]
            rodadas = 3
            rodada = 1
            pontos_1 = 0
            pontos_2 = 0
            while rodadas > 0:
                print("**** Rodada",rodada,"****\n")

                n = int(input("Quantas peças terá no tabuleiro? "))
                m = int(input("Limite de peças por jogada? "))
                if n < m:
                    m = n
                vez_de_jogar = "N"
                jogada_1 = 0
                jogada_2 = 0
                jogadas = ["1", "2"]
                jogada = random.choice(jogadas)
        # ////////////////////////////////////////////////////////////////////////////////////////////////////////////
                if jogada == "1":
                    print(f"{nome_jogador_1} começa!\n")
                    vez_de_jogar = "1"
                else:
                    print(f"{nome_jogador_2} começa!\n")
                    vez_de_jogar = "2"
        # ////////////////////////////////////////////////////////////////////////////////////////////////////////////
                while n > 0:
                    if vez_de_jogar == "1":
                        print(f"Vez de {nome_jogador_1}\n")
                        jogada_1 = usuario_escolhe_jogada(n , m)
                        n = n - jogada_1

                        vez_de_jogar = "2"
                        ganhador.append("1")

                        if jogada_1 == 1:
                            print(f"{nome_jogador_1} tirou uma peça.\n")
                        else:
                            print(f"{nome_jogador_1} tirou",jogada_1,"peças.\n")

                        if n == 1:
                            print("Agora resta apenas uma peça no tabuleiro.\n")
                        else:
                            print("Agora restam",n,"peças no tabuleiro.\n")

        # ////////////////////////////////////////////////////////////////////////////////////////////////////////////
                    elif vez_de_jogar == "2":
                        print(f"Vez de {nome_jogador_2}\n\n")

                        jogada_2 = usuario_escolhe_jogada(n , m)

                        n = n - jogada_2
                        vez_de_jogar = "1"
                        ganhador.append("2")

                        if jogada_2 == 1:
                            print(f"{nome_jogador_2} tirou uma peça.\n")
                        else:
                            print(f"{nome_jogador_2} tirou",jogada_2,"peças.\n")

                        if n == 1:
                            print("Agora resta apenas uma peça no tabuleiro.\n")
                        else:
                            print("Agora restam",n,"peças no tabuleiro.\n")
        # ////////////////////////////////////////////////////////////////////////////////////////////////////////////                       
                placar = ganhador.pop()
                if placar == "1":
                    print(f"Fim do jogo! {nome_jogador_1} ganhou!\n")
                    pontos_1 += 1
                    rodada += 1
                    rodadas -= 1

                elif placar == "2":
                    print(f"Fim do jogo! {nome_jogador_2} ganhou!\n")
                    pontos_2 += 1
                    rodada += 1
                    rodadas -= 1
            print("**** Final do campeonato! ****\n")
            print(f"\nPlacar: {nome_jogador_1} | {pontos_1} X {pontos_2} | {nome_jogador_2}")

partida()
