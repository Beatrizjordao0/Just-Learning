# Jogo do trenzinho

import random
# sentenças

s1 = '4 bebês'
s2 = 'Amor da sua vida'
s3 = 'Cientista que descobriu a cura do cancer'
s4 = 'Um dinossauro bonzinho e amoroso abandonado'
s5 = 'Um menino que será adotado amanhã'
s6 = 'Um grupo de idosos'

s7 = 'Um serial killer'
s8 = 'Professor que te reprovou na quinta série em artes'
s9 = 'Kraken atacando seu parceiro amoroso'
s10 = 'Seu chefe'
s11 = 'Cavaleiro Medieval'
s12 = 'Menino que fazia bullying com você aos 5 anos de idade'

sentencasboas = [s1, s2, s3, s4, s5, s6]
sentencasruins = [s7, s8, s9, s10, s11, s12]

jogar = 'y'

while jogar == 'y':
    # Escolhas
    escolhasboas = random.sample(sentencasboas, 2)
    escolhasruins = random.sample(sentencasruins, 2)
    # bom
    escolhaboa1 = escolhasboas[0]
    escolhaboa2 = escolhasboas[1]
    # ruim
    escolharuim1 = escolhasruins[0]
    escolharuim2 = escolhasruins[1]

    print(f'\nTrilho 1 --> {escolharuim1} e {escolhaboa1}\n')
    print(f'Trilho 2 --> {escolhaboa2} e {escolharuim2}\n')


    resposta = input(f'Em qual trilho você vai passar?(1/2) --> ')

    if resposta == '1':
        print(f'Você matou {escolharuim1} e {escolhaboa1}')
    else:
        print(f'Você matou {escolharuim2} e {escolhaboa2}')

    jogar = input('Vai querer jogar denovo?y/n --> ').lower()
    
    
    
    
    



