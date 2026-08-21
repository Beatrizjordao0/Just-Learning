#Receber uma palavra ou uma frase e dizer quantas vogais tem nessa frase ou palavra


texto = input('\033[36mDigite algum texto sem colocar o acento: \n')
vogais = 0
for v in texto:
    if v == 'a' or v == 'e' or v == 'i' or v == 'o' or v == 'u':
        print('\033[32m',end=' ')
        vogais += 1
    else:
        print('\033[31m', end=' ')
    print(v, end='')

print(f'\n\033[0mO seu texto tem {vogais} vogais')