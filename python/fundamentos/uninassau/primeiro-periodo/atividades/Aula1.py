valor_emprestimo = float(input("Digite o valor do empréstimo solicitado: "))
salario_cliente = float(input("Digite o valor do seu salário: "))
meses = int(input("Em quantos meses você deve pagar o empréstimo? "))
#-----------------------------------------------------------------------------
teto = (30/100) * salario_cliente
prestacao_mensal = valor_emprestimo / meses
#///////////////////////////////////////////////////////////////////////////////////////
if prestacao_mensal > teto:
    print("Seu empréstimo não foi aprovado!\nSabe por que? Vou te explicar\n")
    print(f"Você pediu um valor de {valor_emprestimo}, mas você só ganha {salario_cliente}\n"
          f"O valor da prestação mensal ficou em {prestacao_mensal}, o que\n"
          f"ultrapassa 30% do seu salário que é de {teto}.")
else:
    print("Seu empréstimo foi aprovado")
