from Pessoa import Pessoa


class Cliente(Pessoa):
    carrinho: list

    def __init__(self, nome, cpf, endereco, carrinho):
        super().__init__(nome, cpf, endereco)
        self.carrinho = carrinho
