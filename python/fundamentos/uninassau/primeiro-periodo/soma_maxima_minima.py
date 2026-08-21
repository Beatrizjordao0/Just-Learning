# Fazer um programa que caucule a soma máxima e a soma mínima de uma lista de valores aleatórios.

def soma_max(valores):
    nmrs_positivos = []
    for valor in valores:
        if valor > 0:
            nmrs_positivos.append(valor)
    print(f"Os números a serem somados para a soma máxima são {nmrs_positivos}")
    soma = 0  
    for nmrs in nmrs_positivos:
        soma += nmrs
    
    return soma


# /////////////////////////////////////////////////////////////////////////////////////////////////

def soma_min(valores):
    nmrs_negativos = []
    for valor in valores:
        if valor < 0: # Se o valor for menor do que o 0 
            nmrs_negativos.append(valor)
    print(f"Os números a serem somados para a soma mínima são {nmrs_negativos}")
    soma = 0  
    for nmrs in nmrs_negativos:
        soma += nmrs
    
    return soma

# /////////////////////////////////////////////////////////////////////////////////////////////////
# ***** PRONTO👍 *****
def recebe_valores():
    i = 1
    valores = []
    entrada = input(f"Digite o {i}º número: (aperte 'enter' para sair) ")
    while True:
        if entrada == "":
            break
        try:
            valor = int(entrada)
            i += 1
            valores.append(valor)
            entrada = input(f"Digite o {i}º número: (aperte 'enter' para sair) ")
        except:
            print("Digite um número válido. ")
            entrada = input(f"Digite o {i}º número: (aperte 'enter' para sair) ") #ERRO RESOLVIDO👍

    return valores


# /////////////////////////////////////////////////////////////////////////////////////////////////

def main():
    valores = recebe_valores()
    max_soma = soma_max(valores)
    min_soma = soma_min(valores)
    
    return f"A soma máxima é: {max_soma}\nA soma mínima é: {min_soma}."

# /////////////////////////////////////////////////////////////////////////////////////////////////


print(main())

