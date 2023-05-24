from Endereco import Endereco


class Pessoa:
    nome: str
    cpf: int
    endereco: Endereco

    def __init__(self, nome, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco

    def get_nome(self):
        return self.nome

    def get_cpf(self):
        return self.cpf

    def get_endereco(self):
        return self.endereco

    def set_nome(self, nome):
        self.nome = nome

    def set_cpf(self, cpf):
        self.cpf = cpf

    def set_endereco(self, endereco):
        self.endereco = endereco
