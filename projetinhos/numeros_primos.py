def n_primos(n):
    numeros = 0
    for numero_que_sera_testado in range(2, n + 1):
        eh_primo = True
        for numero_que_testara in range(2, numero_que_sera_testado):
            if numero_que_sera_testado % numero_que_testara == 0:
                eh_primo = False
                break
        if eh_primo:
            numeros += 1
    return numeros

print(n_primos(50))


