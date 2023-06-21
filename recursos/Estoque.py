from classes.Produto import Produto


class Estoque:
    produtos = [
        {
            produto: Produto("Arroz", 5.99),
            quantidade: 100,
        },
        {
            produto: Produto("Feijão", 6.99),
            quantidade: 50,
        },
        {
            produto: Produto("Macarrão", 3.99),
            quantidade: 100,
        },
        {
            produto: Produto("Sabonete", 1.99),
            quantidade: 100,
        },
    ]

    def __init__(self, produtos):
        self.produtos = produtos

    def aumentar_estoque(self, produto, quantidade):
        for prod in self.produtos:
            if prod.get("produto").get_id() == produto.id:
                prod["quantidade"] += quantidade
                return
        print("Produto não encontrado no estoque")

    def diminuir_estoque(self, produto, quantidade):
        for prod in self.produtos:
            if prod.get("produto").get_id() == produto.id:
                prod["quantidade"] -= quantidade
                return
        print("Produto não encontrado no estoque")

    def encontrar_produto(self, cod):
        for prod in self.produtos:
            if prod.get("produto").get_id() == produto.id:
                return prod
        return None
