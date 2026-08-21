'''
Primeiro programa em pycharm
aprendendo com Bro code
06/02/24 19:40
Beatriz Jordão
'''

#---------------------------------------------------------------------------------
#|                            Variáveis e strings                                |
#---------------------------------------------------------------------------------
#Uma variável é um baú de algum valor.
#Quando atribuído um valor para essa variávelmanto7
#ela vai atuar como esse valor.

#----------------------------------------------------------------------------------

#strings são um conjunto de caracteres sem valor algum.
#Toda string deve estar dentro de aspas simples ou duplas.
#Quando usado o sinal de igual;
#o que estiver do lado esquerdo vai "virar" o que tem do lado direito.
#nome agora significa Beatriz.
'''
nome = "Beatriz"
'''
#-----------------------------------------------------------------------------------

#imprime a variável pelo seu valor.
'''
print(nome)
'''

#-------------------------------------------------------------------------------------

#imprime uma string e uma variável.
#pode usar tanto a vírgula como o mais para juntar os dois.
#ex: ("olá", nome) //// ("olá" + nome)
'''
print('Olá,', nome)
'''
#---------------------------------------------------------------------------------------

#type mostra o tipo da variável.
#existem vários tipos de variáveis. EX:
#bool = True ou False;
#int = 1, 2, 3, 40, 1000;
#string = tudo o que estiver entre aspas;
#float = 0.6; 100.98;
'''
print(type(nome))

int = 2
float = 3.5

print(type(int))
print(type(float))
'''

#--------------------------------------------------------------------------------------7

#para concatenar (usando o +) variáveis com palavras
#é preciso todos terem o mesmo tipo:
'''
idade = 20

print("Sua idade é: " +  str(idade))
'''
#com a vírgula, não há necessidade disso:
'''
print("Sua idade é:", idade)
'''
#------------------------------------------------------------------------------------
#|                multiple assignment = atribuição múltipla                         |
#------------------------------------------------------------------------------------
'''
nome = Beatriz
idade = 16
estudante = True
'''
#------------------------------------------------------------------------------------------------------

'''
nome, idade, estudante = "Beatriz", 16, True
'''
#-------------------------------------------------------------------------------
#|                 Coisas que podemos fazer com uma str;                       |
#-------------------------------------------------------------------------------

#comando len conta quantas letras tem a string
'''
nome = "Beatriz"
print(len(nome))
'''
#a primeira posição é sempre 0
'''
nome = "Bibia"

print(nome.find("a")) = acha a posição da letra especificada
print(nome.capitalize()) = Bota a inicial em maiúsculo
print(nome.upper()) = todas maiúsculas
print(nome.lower()) = todas minúsculas
print(nome.isdigit()) = verifica se tem algum número nessa string
print(nome.isalpha()) = verifica se todas são letras do alfabeto
print(nome.count("i")) = você da uma letra e ele diz quantas tem na sua string
print(nome.replace("i", "o") = muda uma letra pela outra
'''

#repete a string n vezes
'''
print(nome * 5)
'''
#______________________________________________________________________________________
#|                        type casting = conversão de tipo                            |
#--------------------------------------------------------------------------------------
'''
x = 1 #int
y = 2.0 #float
z = "3" #string

print(str(x))
print(int(z))
print(str(y))
'''
#_________________________________________________________________________________________
#                                  Perguntando                                           |
#-----------------------------------------------------------------------------------------

#comando input pergunta e devolve uma string
'''
nome = input("Qual seu nome?\n")
idade = int(input("Quantos anos você tem?\n"))
cidade = input("Em qual cidade você reside?\n")
feedback = input("Você está satisfeito(a) com o prefeito?\n")

if feedback == "S" or "s" or "sim" or "Sim":
    print(nome, "está satisfeito(a) com o prefeito.")
else:
    print(nome, "não está satisfeita com o prefeito.")
'''
#_________________________________________________________________________________
#|                               Funções de math                                 |
#---------------------------------------------------------------------------------

#import math
#float = 9
'''
#print(round(float)) = arredonda o número
#print(math.ceil(float)) = arredonda o número para cima
#print(math.floor(float)) = arredonda para baixo
#print(abs(float)) = mostra a distância de um número e 0
#print(pow(float,2)) = eleva a variável pelo número escrito depois da vírgula
#print(math.sqrt(float)) = raíz quadrada de um número
#print(max(a, b, c)) = diz qual o maior valor entre números
#print(min(a, b, c)) = diz qual o menor valor entre números
'''

#___________________________________________________________________________________
#|                              Partindo variáveis                                 |
#-----------------------------------------------------------------------------------

#slicing = cria uma substring partindo a string original e partes desejadas
#                        indexing[] or slice()
#                             [start:stop:step]
#start é inclusivo e o stop é exclusivo(em relação as posições)
'''
nome = "Beatriz Jordão"
'''

#posso deixar [:8] pois quando n tem o número ele assume que é 0
#do mesmo jeito [8:] Quando n tem número vai até p último

'''
Primeiro_nome = nome[:8]
sobrenome = nome[8:15]
nome_2 = nome[::3] = step recebe um número e conta as vezes para pular
reversed_name = nome[::-1]

print(Primeiro_nome)

'''
#slice funciona basicamente do mesmo jeito
#mas, ao invés de usar dois pontos, vamos usar uma vírgula para separar.
#se contarmos da esquerda para a direita --> usaremos números positivos;
#mas, se contarmos da direita para a esquerda <-- serão negativos.
'''
website = "http://google.com"
website_2 = "http://wikipedia.com"
'''
#primeiro cria a função e depois aplica.
#o nome da função eu posso escolher, mas vai ficar slice mesmo.
# a gente corta de frente pra trás e de trás pra frente,
#pra pegar o nome do meio.
'''
slice = slice(7,-4)

print(website[slice])
print(website_2[slice])
'''

#__________________________________________________________________________
#|                             IF, ELIF, ELSE                             |
#--------------------------------------------------------------------------

#requisitos para ganhar sacolinha

#boas vindas
'''
print("Bem vindo(a) ao meu aniversário! Preencha as perguntas "
      "para que saibas se podes receber uma sacolinha!!\n")
'''
#perguntas
'''
nome = input("Qual seu nome?\n")
idade = int(input("Quantos anos você tem?\n"))
'''
#apenas crianças de 1 a 8 anos de idade podem receber sacolinha
#se você tem até 14 anos e me conhece. você pode receber sacolinha.
'''
if idade <= 8:
    print("Tome uma sacolinha e se divirta na minha festa!!")
elif idade < 14:
    print("Só pode entrar se me conhecer.\n")
    me_conhece = input("Qual o meu nome?")
    if me_conhece == "Beatriz":
        print("Que bom te ver", nome,". Toma uma sacolinha e vamos nos divertir")
    else:
        print("Aparta-te de mim que eu não vos conheço.")
else:
    print("Aparta-te de mim que eu não vos conheço.")
'''
#________________________________________________________________________________________
#|                              😶‍🌫️ operadores lógicos😶‍🌫️                                     |
#----------------------------------------------------------------------------------------

#and, or, not
'''
print("OII! meu nome é Beatriz e eu vou te fazer uma pergunta!")

nome = input("Qual meu nome?\n")

if nome == "Beatriz" or nome == "beatriz":
    print("Você acertou! meu nome é esse mesmo!")
else:
    print("Você errou... mais sorte na próxima vez.")

print("agora começa de verdade.\n")
print("1. lá em casa está fazendo muito frio!! eu derrubei a água e ela congelou!!\n"
      "Sabendo a temperatura em que a água congela e levando em consideração que\n"
      "a temperatura máxima que pode ser atingida é -10, responda:\n"
      "Qual a temperatura aproximada da minha casa?")
temp = int(input("R:"))

if temp <= 0 and temp >=-10:
    print("Acertou!! Muito bem. se prepare para a próxima!!!")
else:
    print("Puxa... você errou. cê é ruim hein....")

print("Última pergunta.\n")
print("2. Eu tenho 1.65 m. Minha mãe tem 1.67m. Minha vó tem 1.50m.\n"
      "Qual de nós 3 é mais alta?")
print("a) Eu\n"
      "b) Mãe\n"
      "c) Vó\n")

altura = (input("R:"))

if not altura == "b":
    print("Você errou!!")
else:
    print("Boaa muleke! acertou pae.")

print("Foi bom ver como você se saiu. Obrigada por ter jogado esse joguinho de teste.\n"
      "Jesus te ama!\n"
      "Tchau!!")
'''

#____________________________________________________________________________________
#|                             ➿Loops while and for➿                              |
#------------------------------------------------------------------------------------



#                          === WHILE LOOP ===


#pergunta ao usuário se quer guardar o papel ou se vai cortar
#G = guardar, C = cortar, S = sair
#conta quantos papeis foram guardados e tira os que forem cortados
'''
print("Olá, bem vindo a papelaria.\n"
      "Seu trabalho aqui será cuidar dos papeis que chegam.\n"
      "Você decidirá o que fazer com eles.\n"
      "Digite G para guardar, C para cortar ou S pra sair.")

print("Seu primeiro papel chegou!\n"
      "Decida o que fazer!! ")

papel = 1

while True:
    ação = input("O que você vai fazer com o papel?\n"
                 "G, C, S\n")
    if ação == "G":
        papel = papel + 1
        print("Você guardou o papel na gaveta!\n"
              "Sua gaveta tem",papel,"papeis.")

    elif ação == "C":
        papel = papel - 1
        print("Você decidiu cortar o papel.\n"
              "O número de papeis na sua gaveta é:",papel)
    elif ação == "S":
       print("Foi bom trabalhar com você. Até depois!")
       break

    elif papel == 0:
        print("Você ta sem papel na gaveta!\n"
              "aperte S se quiser sair.")
    else:
        print("Digite uma letra válida.")

'''
#--------------------------------------------------------------------------------------------------------
#                            ===FOR LOOP===

#vai repetir um número finito de vezes
'''
for i in range(10):
     print(1)
'''

#50 mostra onde vai iniciar,
# 100 mostra até onde eu quero ir e o dois é como eu vou
#o terceiro número depois da vírgula significa
# que o meu programa vai contar de 2 em 2
#lembrando sempre que o programa começa pela posição 0.
#ent meu programa só vai contar até 98,
#já que 50 representa 0 e não 1, e também
#eu to contando de dois em dois.
#Então para chegar em 100 é só adicionar 1, ou mudar para 101
'''
for i in range(50, 101, 2):
    print(i)
'''

# O i é uma variável que representa cada elemento na repetição.
#se for uma lista, o i vai receber o valor de todos e devolver
# aquele que o usuário pedir
#se for uma palavra como abaixo e eu não especificar a
# letra que eu quero,
#ele devolve todas
#ou se eu botar dentro de uma variável,
#ele devolve n vezes,
# sendo n a quantidade de caracteres que aquela palavra tem
# se eu especificar,
# a posição ele devolve apenas oque eu especifiquei.
'''
for i in "Bibia":
    print(i)
    
nome = "Bibia"
for i in nome:
    print(nome)
'''
#aqui em cima ↑ eu defini a posição 0 para imprimir, que seria a letra 'B'.
#O programa executou o 'B' 5 vezes, pois é a quantidade de caracteres
#que tem dentro da variável nome.
'''
import time

for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)
print("Jesus voltou!!")
'''

#_______________________________________________________________________________________________
#|                                         🤜Nested loops🤛                                    |
#-----------------------------------------------------------------------------------------------

#O que são nested loops?
#nada mais nada menos do que um loop dentro de outro
#pode ser com for ou com while! Não importa qual seja.
#O loop que está dentro vai terminar todas as suas iterações, isto é, seus ciclos
#Depois que o loop de dentro terminar, o loop de fora vai começar a rodar

'''
horizontal = int(input("Quantos caracteres você quer na horizontal?\n"))
vertical = int(input("Quantos você quer na vertical?\n"))
caractere = input("Qual o caractere que você quer usar?\n")

for i in range(vertical):
    for j in range(horizontal):
        print(caractere, end="")
    print()
'''
#print() só cria uma nova linha em branco

#__________________________________________________________________________________________________________
#|                                     💪 Loop control Statements💪                                       |
#----------------------------------------------------------------------------------------------------------


# Declarações de controle de um loop

#Pra que serve??
#Muda a execução de uma sequêcia normal do loop.

#break = Para o loop completamente
#continue = passa pro próximo caractere do loop
#pass = não faz nada(cópia mal feita do continue)
'''
while True:
    nome = input("Qual seu nome?\n")
    if nome != "":
        break
'''
#--------------------------------------------------------------------------------------------
'''
numero_celular = "(81) 99837-8407"

for i in numero_celular:
    if i == "(" or i == ")" or i == "-" or i == " ":
        continue
    print(i, end="")
'''
#----------------------------------------------------------------------------------------------
'''
for i in range(1, 21):
    
    if i == 13:
        pass
    else:
        print(i)
'''



#__________________________________________________________________________________________________________
#|                                           📃 LISTAS 📃                                                 |
#----------------------------------------------------------------------------------------------------------

#basicamente você pode guardar várias informações dentro de uma variável separando por uma vírgula
#Deve começar por um colchete
'''
comidas = ["Macarronada", "Strogonoff", "Picanha", "Hamburguer", "Pizza", "Purê", "Batata frita"]
                 0             1            2           3           4        5           6
'''
#  ===Propriedades das Listas===

#comidas.pop() = tira o ultimo item
#comidas.append("Sorvete") = adiciona mais um item
#comidas.remove("Pizza") = tira determinado item
#comidas.insert(0,"bolo") = adiciona um item em determinada posição
#comidas.sort = mistura alfabeticamente os itens da lista
#comidas.clear = apaga tudo
'''
for comida in comidas:
    print(i)

comidas[1] = "frango"
'''
# acima ↑ posso substituir um item em determinada posição por outro
#com essa linha de comando, a posição 1 que antes era ocupada por strogonoff,
#agora será frango.

#--------------------------------------------------------------------------------------------------

#             ===Listas 2D = Lista de outra lista===
'''
bebida = ["coca", "pepsi", "guaraná"]
#           0        1         2

janta = ["Strogonoff", "Hamburguer", "Pizza"]
#             0             1           2

sobremesa = ["bolo", "sorvete"]
#              0         1

comida = [bebida, janta, sobremesa]
#           0       1         2
'''
#o primeiro colchete abaixo remete a qual posição o usuário quer escolher e isso significa umas das listas
#o outro colchete é a posição da comida que está dentro da lista 0.
'''
print(comida[0][2])
'''
#---------------------------------------------------------------------------------------------------------

#                ===TUPLAS===

#tuplas = Coleção ordenada e imutável
#           usada para agrupar informações relacionadas

#parecido com a lista, mas pode agrupar informações de tipos diferentes
#usada com parenteses

'''
estudante = ("Beatriz", 17, "Feminino","SESI")
#                0       1       2        3
'''
#estudante.count("Beatriz") = conta quantas vezes beatriz aparece na tupla
#estudante.index("SESI") = mostra a posição em que o nome SESI aparece

#      ===SET===

#Set = é como uma lista, mas é desorganizado, não aceita o mesmo valor
#é usado com chaves 
#A ordem das palavras pode mudar
'''
set = {"Faca", "Colher", "Garfo"}
set_2 = {"Copo", "Tijela", "Prato", "Faca"}
'''
#   ===Propriedades de SETs===

#set.add("Guardanapo") = adiciona um novo item
#set.remove("Faca") = retira um item
#set.clear() = limpa tudo
#set.update(set_2) = junta os dois sets
#mesa = set.union(set_2) = junta os dois sets em uma variável
#print(set.difference(set_2)) = vê o que um set tem que o outro não tem.
#print(set.intersection(set_2)) = Vê o que eles têm em comum
'''
for x in mesa:
    print(x)
'''
#------------------------------------------------------------------------------------------------------------

#______________________________________________________________________
#|                             DICTIONARY                           |
#-----------------------------------------------------------------------

#O que é?

#É uma coleção única de um par chave:valor
#É mutável, e não é ordenada
#é rápido porque usa hash, que permite acessar um valor rapidamente

#abaixo ↓ podemos ver a chave:valor
'''
capital = {'EUA':'Washington DC',
           'Brasil':'Brasília',
           'Russia':'Moscow'}

#Atualiza a lista(adiciona ou só modifica)
'''
#capital.update({'Alemanha':'Berlim'})
#capital.update({'EUA':'Nova Iorque'})
'''
#Para chamar uma capital só precisamos acionar a chave principal
'''
#print(capital['Brasil'])
'''

#do jeito de cima é mais difícil se a gnt não souber quais países tem
#Portanto um jeito de ajudar é usando o comando abaixo
#capital.get é como se fosse uma pergunta:
#"Tem Alemanha? se tiver printa, se não tiver não faz nada
'''
#print(capital.get('Alemanha'))
'''
#print(capital.keys()) = mostra apenas as chaves primárias
#print(capital.values()) = mostra apenas os valores das chaves
#print(capital.items()) = mostra as chaves e os valores
#capital.pop('EUA') = retira o item
for x,y in capital.items():
    print(x, y)
'''
#-----------------------------------------------------------

#      === Index operator [] ===
#          ⌊ permite o acesso a elementos sequenciais:
#             (str, list, tuples)

'''
nome = 'beatriz'

if nome[0].islower():
    nome = nome.capitalize()
'''

#capitalize = aumenta somente a primeira letra
#para capitalizar a palavra inteira usa-se upper

'''
first_name = nome[0:7].upper()
'''
#print(first_name)

#last_character = name[-1]
#Ao adicionar -, começa-se a contar pelo lado oposto


'''
Beatriz Jordão
python full course for free(on youtube)
1h 53min 28sec
bye
'''