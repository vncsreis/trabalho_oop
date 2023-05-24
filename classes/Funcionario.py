from Pessoa import Pessoa


class Funcionario(Pessoa):
    id_funcionario: int

    def __init__(self, nome, cpf, endereco, id_funcionario):
        super().__init__(nome, cpf, endereco)
        self.id_funcionario = id_funcionario
