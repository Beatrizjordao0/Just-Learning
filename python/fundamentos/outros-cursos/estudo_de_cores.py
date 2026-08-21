#Estudando o sistema de cores do python

#tem que se começar dessa forma:

# print('\033[m')

#antes do m tem que se escolher o estilo da frase, a cor e o backgound

#para redefinir tudo é só fazer a mesma coisa ao contrário
#print('\033[40m Frase de teste\033[0m
         # \033[0m
         #   ↪ uso isso para redefinir tudo para o normal

#\033[40;1;30m
    # |  |  \_ cor da fonte. Vai de 30 até 37
    # |   \_ Estilo da letra. 0 para normal e 1 para negrito. São os únicos.
    #  \_Cor do background. Vai de 40 até 47

# Tabela de cores
#  0 - branco
# 30 - Preto
# 31 - vermelho
# 32 - verde
# 33 - amarelo
# 34 - azul
# 35 - lavanda
# 36 - ciano
# 37 - cinza

# A tabela de cores do background segue a mesma ordem

print('\033[31;1;44mAté mais\033[0m Opa amigos')

#percebe-se que após fechar com o \033[0m o Opa amigos fica sem cor. Antes de fechar tem cor, mas depois
#zera todas as formatações de cor e estilo

