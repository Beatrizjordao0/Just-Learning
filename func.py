print("Calculadora")

def soma():
    total = 0
    numeros = int(input("Quantos números você quer somar? "))
    for i in range(numeros):
        num = float(input(f"Digite o {i+1}º número: "))
        total += num
    return total  # Retorna o resultado ao invés de imprimir

def subtrai():
    numeros = int(input("Quantos números você quer subtrair? "))
    resultado = float(input("Digite o primeiro número: "))
    for i in range(numeros - 1):
        num = float(input(f"Digite o próximo número: "))
        resultado -= num
    return resultado

def multiplica():
    resultado = 1
    numeros = int(input("Quantos números você quer multiplicar? "))
    for i in range(numeros):
        num = float(input(f"Digite o {i+1}º número: "))
        resultado *= num
    return resultado

def divide():
    resultado = float(input("Digite o primeiro número: "))
    numeros = int(input("Quantos números você quer dividir? ")) - 1
    for i in range(numeros):
        num = float(input(f"Digite o próximo número: "))
        if num == 0:
            print("Erro: Divisão por zero não permitida.")
            return None
        resultado /= num
    return resultado

while True:
    print("\n1 - Adição  //  2 - Subtração  //  3 - Multiplicação  //  4 - Divisão")
    operacao = input("Qual operação você quer fazer? ")

    resultado = None  # Inicializa a variável

    if operacao == "1":
        resultado = soma()
    elif operacao == "2":
        resultado = subtrai()
    elif operacao == "3":
        resultado = multiplica()
    elif operacao == "4":
        resultado = divide()
    else:
        print("Escolha inválida!")
        continue  # Volta para o início do loop

    if resultado is not None:
        print(f"Resultado: {resultado}")

    continuarOperacao = input("\nGostaria de continuar?\n 1 - Sim  //  2 - Não \n")

    if continuarOperacao == "2":
        print("Terminando...")
        break
