
'''
Aula 01/03/2024
SESI SENAI
Beatriz e Gabriel
'''


#-----------1----------------------------
'''
a = int(input('Digite um número para a soma:\n'))
b = int(input('Digite outro número:\n'))

print('A soma de',a,'e',b,'é:',a + b)
'''
#-----------2----------------------
'''
a = int(input('Quantos alunos tem na sua classe?\n'))
nota = 0
for i in range(a):
    notas = int(input('Digite um número:\n'))
    nota = notas + nota


print('A média de 4 alunos é:', nota/a)
'''
#-----------3---------------------
'''
nmr = float(input('Digite um número em metros:\n'))

cm = nmr * 100

print(nmr,'m em cm é igual a:',cm)
'''
#-----------4--------------------
'''
raio = float(input('Digite um número para o raio de um círculo:\n'))

area = 3.14 * raio ** 2

print(f'A área do círculo é: {area}')
'''
#------------5-----------------
'''
lado = float(input('Qual a medida do lado de um quadrado?\n'))
area = lado * lado

print(f'O dobro da área do seu quadrado é: {area*2}')
'''
#-------------6-----------------------
'''
F = float(input('Me diga a temperatura em Farenheit:\n'))
temperatura_C = 5 * ((F - 32)/9)
temperatura_C = round(temperatura_C,2)

print(f'A temperatura {F} F em Graus celcius é {temperatura_C} C.')
'''
#-------------7------------------------
'''
int1 = int(input('Digite um número inteiro:\n'))
int2 = int(input('Digite outro número inteiro:\n'))
float = float(input('Digite um número com vírgula:\n'))
float = float ** 3
float = round(float,2)

print('O produto do dobro do primeiro com metade do segundo é:',(int1 * 2) * (int2/2))

print('A soma do triplo do primeiro com o terceiro é:',(3*int1) + float)

print('O terceiro elevado ao cubo é:',float)
'''

