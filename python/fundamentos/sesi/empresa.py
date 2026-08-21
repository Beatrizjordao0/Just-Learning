'''Desafio: Fazer uma enquete que pergunte entre 6 SOs e retorne a porcentagem de voto em cada uma'''
#passo a passo:
#passo 1: perguntar várias vezes pro usuário qual SO ele prefere
#passo 2: Armazenar todas as respostas em uma lista
#passo 3: Ver a quantidade de cada um e mostrar a porcentagem

print('Escolha o melhor sistema operacional digitando o número correspondente:\n'
      '1 - Windows Xp\n'
      '2 - Unix\n'
      '3 - Linux\n'
      '4 - Netware\n'
      '5 - Mac OS\n'
      '6 - outro\n'
      'Digite 0 se quiser parar o sistema.\n')

votos = []

while True:
    voto = int(input('Na sua opnião qual o melhor sistema operacional? '))
    votos.append(voto)
    if voto == 0:
        break

total = len(votos)
#--------------------------------
contador = {i:votos.count(i)    #
            for i in range(1,7)}#
#--------------------------------
#nota de entendimento do bloco acima:
#o for diz que o i vai ser 6 números diferentesz
#embora tenha vindo depois do outro comando,
#o for vai ser o primeiro a ser iterado.
#Então o i: vai ser o mesmo i que for o i do for
#votos.count(i) -> Como i vai mudar entre 6 números diferentes,
#ele conta a quantidade de vezes que o número da vez apareceu.
#ex:
#quando i for 1:
#   -> 1:quantidade de vezes que 1 aparece
#e assim é com o resto dos números.

for numero, aparecimentos in contador.items():
    percentual = aparecimentos * 100 / total

    print(f'O percentual de respostas do número {numero} é: {percentual:.2f}%')

