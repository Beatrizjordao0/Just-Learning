#_____________________________________________________________________________________
#   |                              Funções                                   |
#----------------------------------------------------------------------------------


#Uma função é um bloco de código que só será executada quando for chamada


#↱ Função
#|   ↱ Nome da Função
#|   |      ↱variável temporária. Apenas guarda o lugar para o argumento
#def hello(nome):
    #print('Olá,',nome)

# ↱ Chamada da função
# |       ↱Argumento. O nome lá em cima foi substituído por esse argumento
#hello('Beatriz')

'''
times = int(input('Quantas vezes quer repetir?\n'))
def repet(a):
    for i in range(times):
        print('hi!', end='')

repet(times)
'''

#def filhos(a,b,c):
#   print("A filha mais velha de Sheila é",a)
#   print("A filha do meio é",b)
#   print('O filho mais novo é',c)

#filhos("Larissa", "Beatriz", "Thomas")


#           === Declaração Return ===

# ↪ Essa função meio que transforma a função em uma variável
# ↪ quando o return é chamado, o valor que ele retorna vai para a função
# tipo assim:

#a = int(input('Digite um número a ser multiplicado:\n'))
#b = int(input('Digite outro número a ser multiplicado:\n'))

#def multiplicação(x,y):
#    return x * y

#resultado = multiplicação(a,b)
# Aqui eu vou ter de usar uma variável para guardar o valor da função porque
# eu usei a função return mais cedo no código então ele devolve o valor pra função

#print(resultado)

#  === KEYWORD ARGUMENTS ===
# ↪ Argumentos com identificador
# ↪ independente da posição, se eu atribuir um argumento àquela posição
# antes estabelecida ele substituirá aquela variável temporária.

#def nome(x, y, z):
#    print('meu nome é: ',x,y,z)

#nome(z='Albuquerque',x='Beatriz',y='Jordão')

# A FUNÇÃO VAI SER EXECUTADA PRIMEIRO.

#          === *args ===

#            ↪ Transforma os argumentos em uma tupla
#             ↪ Super útil porque pode aceitar um número variável de argumentos

#def add(*args):      ↪ Já que a tupla é imutável, se eu quiser alterar qualquer coisa eu preciso
#    soma = 0             transformar ela numa lista: args = list(args)
#    for i in args:               e daí vai se tornar uma lista e agora eu posso escolher
#        soma += i            uma posição e o valor que eu quero atribuir
#    return soma               args[2] = 0

#print(add(1 ,2 ,3 ,4 ,5 ,6))
#          0  1  2  3  4  5   ==  essas são as posições