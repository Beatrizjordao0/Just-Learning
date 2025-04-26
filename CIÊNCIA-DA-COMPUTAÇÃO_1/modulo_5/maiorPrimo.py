"""
Escreva a função {maior_primo} que recebe um número inteiro 
maior ou igual a 2 como parâmetro e devolve o maior número 
primo menor ou igual ao número passado à função

Dica: escreva uma função éPrimo(k) e faça um laço 
percorrendo os números até o número dado checando 
se o número é primo ou não; se for, guarde numa variável.
Ao fim do laço, o valor armazenado na variável é o maior 
primo encontrado.

"""

def éPrimo(k):
    if k < 2:
        return False
    elif k == 2:
        return k
    for n in range(2, k):
        if k % n == 0:
            return False
        
    return k
        
def maior_primo(a):
    if a >= 2:
        numerosPrimos = []
        for n in range(2, a + 1):
            if éPrimo(n) == n:
                numerosPrimos.append(n)

        maior = numerosPrimos.pop()

        return maior
    else:
        return False
    
    
