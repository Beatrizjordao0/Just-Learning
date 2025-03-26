# Criar uma forma de calcular a função binomial.
# n, k = n!/(k! * (n - k)!)

def fatorial(n):
    fat = 1
    while n > 1:
        fat *= n
        n -= 1
    return fat

def funcaoBinomial(n , k):
    return fatorial(n) / (fatorial(k) * fatorial(n - k))

print(funcaoBinomial(20, 10))

    