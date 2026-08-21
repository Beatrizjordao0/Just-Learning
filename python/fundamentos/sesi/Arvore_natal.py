#Fazer uma árvore   ******
             #ex:  ********
             #    **********
#sempre tem um a menos
#o número aumenta
#o número de espaços diminui




#     *
#    ***
#   *****
#  *******

def arvore_de_natal(altura, smbl):
    for i in range(1, altura + 1):
        qntd_espaco = altura - i
        print(" " * qntd_espaco + smbl * (2 * i - 1))

linhas = int(input("Digite a altura da árvore: "))
smbl = input("Digite o símbolo da árvore: ")

arvore_de_natal(linhas, smbl)



