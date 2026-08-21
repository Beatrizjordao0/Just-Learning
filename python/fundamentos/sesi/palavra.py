frase = input('Digita uma frase: ')
pesquisa = input('Digite a palavra que você quer achar dentro da sua frase:')

if pesquisa in frase:
    print(f'{pesquisa} está dentro de frase.')
else:
    print('Não tem isso dentro da frase.')