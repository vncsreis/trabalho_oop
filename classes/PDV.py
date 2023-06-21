from classes.Validacao import Validacao
from classes.Interface import Interface


class PDV(Interface):
    cliente: str | None
    produtos: list
    valor_total: float
    cod_compra = 0

    def compra(self):
        cpf = self.informar_cliente()
        print(f"CPF digitado foi: {cpf}")

    def informar_cliente(self):
        op_cpf = self.input_com_decoracao("Possui cadastro conosco? [S/N]")

        while not Validacao.bool(op_cpf):
            op_cpf = self.input_com_decoracao(
                "Resposta inválida!\nPossui cadastro conosco? [S/N]"
            )

        if op_cpf.upper() == "S":
            cpf = self.input_com_decoracao("Digite o CPF: ")

            while not Validacao.cpf(cpf):
                novamente = self.input_com_decoracao(
                    "CPF inválido. Deseja tentar novamente? [S/N]"
                )

                while not Validacao.bool(novamente):
                    novamente = self.input_com_decoracao(
                        "Resposta inválida. Deseja tentar novamente? [S/N]"
                    )

                if novamente.upper() == "N":
                    cpf = None
                    return cpf

                cpf = self.input_com_decoracao("Digite o CPF novamente: ")

        else:
            cpf = None

        return cpf

    def imprimir_com_decoracao(self, texto):
        self.clear()
        print(
            f"""============================================
                    PDV
============================================
    {texto}
"""
        )

    def input_com_decoracao(self, texto):
        self.imprimir_com_decoracao(texto)
        return input()
