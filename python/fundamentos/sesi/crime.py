'''Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:'''

#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Tinha dívidas com a vítima?"
#"Já trabalhou com a vítima?"

'''O programa deve no final emitir uma classificação sobre a participação da pessoa no
crime. Se a pessoa responder positivamente a 2 questão ela deve ser classificada como 'Suspeita,
caso responda de 3 a 4 é 'Cúmplice', e 5 deve ser 'Assassino'.
Caso contrário, ele será classificado como inocente.'''

from colorama import Fore, Style

print('Olá! Gostaria de me apresentar. Meu nome é Beatriz, sou uma detetive. Meu assistente, Gabriel,\n'
      'estará chegando a qualquer momento(ele foi comprar comida).\n'
      'Estamos investigando um caso de assassinato. O nome da vítima é Martin Burguer King.\n'
      ' Acreditamos que você tinha contato com a vítima.\n')
nome = input('Primeiro de tudo: Qual é o seu nome? ')
print(f'Bom, {nome}, você tem direito de permanecer calado(a) e tem direito a um advogado.\n')
print('Peço que responda apenas com s ou n.')
print('Comecemos.\n')

pergunta1 = input(f'{nome}, você telefonou para a vítima no dia do incidente?')
pergunta2 = input('Esteve no local do crime?')
pergunta3 = input('Você mora perto da vítima?')
pergunta4 = input('Por acaso tinha dívidas com o caro King?')
pergunta5 = input('Já trabalhou com o Martin?')

perguntas = [pergunta1,pergunta2,pergunta3,pergunta4,pergunta5]

if perguntas.count('s') == 2:
    estado = 'Suspeito'
    print(f'{Fore.LIGHTRED_EX}{estado}{Style.RESET_ALL}')
    print(f'Obrigada pelo seu tempo {nome}, infelizmente você terá de ficar conosco até '
          f'mais informações serem averiguadas.')

elif perguntas.count('s') == 3 or perguntas.count('s') == 4:
    estado = 'Cúmplice'
    print(f'{Fore.RED}{estado}{Style.RESET_ALL}')
    print('Você está preso(a) como cúmplice do assassinato. Você tem o direto de permanecer calado,\n'
          'e pode ligar para o seu advogado.')

elif perguntas.count('s') == 5:
    estado = 'Culpado'
    print(f'{Fore.LIGHTBLACK_EX}{estado}{Style.RESET_ALL}')
    print('SEU ASSASSINO(A)!! Você está preso(a) por matar Martin Burguer King. Será sentenciado a 10\n '
          'anos de prisão sem fiança por assassinato! Gabriel!!!! Traga as algemas.')

else:
    estado = 'Inocente'
    print(f'{Fore.GREEN}{estado}{Style.RESET_ALL}')
    print(f'Bom, {nome}, agradeço a sua disponibilidade de vir aqui, você está livre para ir.\n'
          f'Se quiser, Gabriel, meu assistente, está trazendo um almoço.')