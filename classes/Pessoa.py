class Pessoa:
    nome: str
    cpf: int
    cep: int

    def __init__(self, nome, cpf, cep):
        self.nome = nome
        self.cpf = cpf
        self.cep = cep

    def get_nome(self):
        return self.nome

    def get_cpf(self):
        return self.cpf

    def get_cep(self):
        return self.cep

    def set_nome(self, nome):
        self.nome = nome

    def set_cpf(self, cpf):
        self.cpf = cpf

    def set_cep(self, cep):
        self.cep = cep
