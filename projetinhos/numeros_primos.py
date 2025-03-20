"""
p = Número que se altera que vamos usar para testar se ele é primo
n = Número que será alterado também para dividir o p para testar se o p é primo

Como o loop começa a partir do 2, o primeiro número a ser testado será o próprio 2.
Quando p == 2 o loop vai pular, porque o teste de n começa em 2 e vai até o p - 1:
                        for n in range(2, p):
                            if p % n == 0:
                                eh_primo = False
                                break
(Deve-se lembrar que sempre que tiver (n, m) o primeiro é sempre inclusivo e o segundo é exclusivo.
Portanto, o primeiro sempre começa nele mesmo, mas o segundo vai até um valor abaixo do que está.
Ex:
    (1, 10)
    -> 1, 2, 3, 4, 5, 6, 7, 8, 9 <-
    
    (2, 11)
    -> 2, 3, 4, 5, 6, 7, 8, 9, 10) <-
    
    Por isso que no loop que checa se n é primo ou não...
        
    --> for n in range(2, p):
            if p % n == 0:
                eh_primo = False
                break
                
    Usamos apenas até um número anterior de p, pois p é divisível por ele mesmo.
    Entretanto, fazemos diferente no Loop:

    --> for p in range(2, n + 1):
            eh_primo = True
            for n in range(2, p):
                if p % n == 0:
                    eh_primo = False
                    break
            if eh_primo:
                numeros += 1

    O loop de p checa se os números até p são primos.
    Se eu digo que quero os números primos até 25, eu devo contar com o próprio 25.
    Por isso que se adiciona +1 à p.

    Exemplo de execução:
    (Não vamos começar com o 2, porque ele se anula)
    Porque o 2 já é primo, e se anula,
    então a soma = 1
    

    1)
        n = 10
        n_primos(10):
            Para primo sendo um número de 2 até 10, faça:
                eh_primo = Verdade
                Para divisor sendo um número de 2 até um número antes de primo, faça:
                    se o resto da divisão do 3 por 2 for 0, então:
                        eh_primo = Falso
                        Para o loop
                Se for primo, então
                    adiciona 1 à soma

        Como o resto da divisão de 3 por 2 não é 0, então:
            soma = 2
    2)  
        n = 10
        n_primos(10):
            Para primo sendo um número de 2 até 10, faça:
                eh_primo = Verdade
                Para divisor sendo um número de 2 até um número antes de primo, faça:
                    se o resto da divisão do 4 por 2 for 0, então:
                        eh_primo = Falso
                        Para o loop
                Se for primo, então
                    adiciona 1 à soma

        Como o resto da divisão de 4 por 2 é 0, então:
            nada acontece e a soma permanece a mesma coisa.
            soma = 2

    3) 
        n = 10
        n_primos(10):
            Para primo sendo um número de 2 até 10, faça:
                eh_primo = Verdade
                Para divisor sendo um número de 2 até um número antes de primo, faça:
                    se o resto da divisão do 5 por 2 for 0, então:
                        eh_primo = Falso
                        Para o loop
                Se for primo, então
                    adiciona 1 à soma

        Como o resto da divisão de 5 por 2 não é 0, então:
            ele repete até chegar no último:

            --> Para divisor sendo um número de 2 até um número antes de primo, faça:
                    se o resto da divisão do 5 por 3 for 0, então:
                        eh_primo = Falso
                        Para o loop
                Se for primo, então
                    adiciona 1 à soma

        Como o resto da divisão de 5 por 2 não é 0, então:
            ele repete até chegar no último:

            --> Para divisor sendo um número de 2 até um número antes de primo, faça:
                    se o resto da divisão do 5 por 4 for 0, então:
                        eh_primo = Falso
                        Para o loop
                Se for primo, então
                    adiciona 1 à soma
        Como o resto da divisão de 5 por 4 não é 0, e 4 já é o último número, então:
            soma recebe + 1
            soma = 3   
        
[...]

E assim por diante!
"""

def n_primos(n):
    soma = 0
    # ----- Loop de p -----
    for primo in range(2, n + 1):
        eh_primo = True
        # ----- Loop de n -----
        for divisor in range(2, primo):
            if primo % divisor == 0:
                eh_primo = False
                break
        if eh_primo:
            soma += 1
    return soma

print(n_primos(10))


