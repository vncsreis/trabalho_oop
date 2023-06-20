class Produto:
    id: int
    nome: str
    valor: float

    cont_id = 0

    def __init__(self, nome, valor):
        Produto.cont_id += 1
        self.id = Produto.cont_id
        self.nome = nome
        self.valor = valor

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_valor(self):
        return self.valor

    def set_valor(self, valor):
        self.valor = valor
