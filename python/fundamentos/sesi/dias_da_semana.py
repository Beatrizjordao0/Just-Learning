#receber 7 dias da semana e dizer se o dia é útil. Quando for dia útil adiciona o sufixo -feira


dias = []
for i in range(7):
    dia = input('Digite um dia da semana entre 2 e 6 e sábado e domingo: ')
    dias.append(dia)
for d in dias:
    if d == 'domingo' or d == 'sábado' or d == 'sabado':
        print(f'\033[31m{d}\033[0m não é dia útil\n')
    else:
        print(f'\033[33m{d}-feira\033[0m é um dia útil\n')