class Estoque:
    # dictionário de produtos em estoque
    # {produto_id: int, quantidade: int}
    produtos: dict

    def __init__(self, produtos):
        self.produtos = produtos

    def aumentar_estoque(self, produto, quantidade):
        for prod in self.produtos:
            if prod.get("produto") == produto.id:
                prod["quantidade"] += quantidade
                return

        produto_aumentado = {"produto": produto.id, "quantidade": quantidade}
        self.produtos.apppend(produto_coletado)

    def diminuir_estoque(self, produto, quantidade):
        for prod in self.produtos:
            if prod.get("produto") == produto.id:
                prod["quantidade"] -= quantidade
                return
        print("Produto não encontrado no estoque")
