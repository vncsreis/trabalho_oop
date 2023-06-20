from Pessoa import Pessoa


class Funcionario(Pessoa):
    id_funcionario: int
    desc_funcionario = float

    def __init__(self, nome, cpf, endereco, id_funcionario):
        super().__init__(nome, cpf, endereco)
        self.id_funcionario = id_funcionario
        self.desc_funcionario = 0.2

    def get_id_funcionario(self):
        return self.id_funcionario

    def set_id_funcionario(self, id_funcionario):
        self.id_funcionario = id_funcionario

    def get_desc_funcionario(self):
        return self.desc_funcionario

    def set_desc_funcionario(self, desc_funcionario):
        self.desc_funcionario = desc_funcionario
