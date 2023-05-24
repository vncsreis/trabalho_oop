class Estoque:
    # lista de produtos em estoque
    produtos: list

    def __init__(self, produtos):
        self.produtos = produtos

    def coletar(self, produto, quantidade):
        for prod in self.produtos:
            if prod["produto"] == produto.id:
                prod["quantidade"] += quantidade
                return

        produto_coletado = {"produto": produto.id, "quantidade": quantidade}
        self.produtos.apppend(produto_coletado)
