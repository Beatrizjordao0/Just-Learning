class Pedido:
    def __init__(self):
        self.itens = []       
        self.total_pago = 0.0 
        self.status = "Pendente" 
    
    def adicionar_item(self, item, preco):
        self.itens.append((item, preco))  
        self.total_pago += preco    

    
    def calcular_total(self):
        return self.total_pago
    
    def alterar_status(self, novo_status): 
        self.status = novo_status
    
    def exibir_resumo(self):
        print("Itens do Pedido:")
        for item, preco in self.itens:
            print(f"- {item}: R${preco:.2f}")
        print(f"Total a ser pago: R${self.total_pago:.2f}")
        print(f"Status do Pedido: {self.status}")


if __name__ == '__main__':

    meu_pedido = Pedido()

    # Adicionando itens ao pedido
    meu_pedido.adicionar_item("Hambúrguer", 15.0)
    meu_pedido.adicionar_item("Batata Frita", 10.0)
    meu_pedido.adicionar_item("Refrigerante", 5.0)

    # Exibindo resumo do pedido
    print("Resumo do Pedido:")
    meu_pedido.exibir_resumo()

    # Calculando o total a ser pago
    total_a_pagar = meu_pedido.calcular_total()
    print(f"Total a ser pago: R${total_a_pagar:.2f}")

    # Alterando o status do pedido
    meu_pedido.alterar_status("Em preparo")

    # Exibindo resumo atualizado do pedido após alteração
    print("\nResumo do Pedido Atualizado:")
    meu_pedido.exibir_resumo()
