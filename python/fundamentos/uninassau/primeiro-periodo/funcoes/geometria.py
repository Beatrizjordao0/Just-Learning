import math
import random

def area_circulo(r):
    return 3.1415 * (r*r)

def raiz_numero(n):
   return math.sqrt(n) 

def hipotenusa(cat1, cat2):
    return math.sqrt((cat1*cat1) + (cat2*cat2))

def volume_cilindro(r, h):
    return 3.1415 * (r*r) * h

def sorteio_ganhadores(nomes):
    ganhadores = []
    for i in range(3):
        ganhadores.append(random.choice(nomes))

    return ganhadores


