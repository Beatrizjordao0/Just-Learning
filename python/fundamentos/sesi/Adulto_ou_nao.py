ano = int(input('Qual ano você nasceu?'))
idade = 2024 - ano
print(idade)

if idade >= 18:
    print('Você é adulto.')
elif idade < 18 and idade > 12:
    print('Você é adolescente.')
elif idade <= 12:
    print('Você é uma criança.')
