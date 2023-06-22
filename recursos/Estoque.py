from classes.Produto import Produto


class Estoque:
    id_atual = 1

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

    def cadastrar_produto(self, nome, valor, qtd):
        novo_produto = Produto(nome, valor)
        for p in self.produtos:
            if novo_produto.get_nome().upper() == p.get("produto").get_nome():
                print("Produto já cadastrado! Tente novamente com outro produto.")
                return
        self.produtos.append({produto: novo_produto, quantidade: qtd})
        print("Produto cadastrado com sucesso.")
