from classes.Validacao import Validacao
from classes.Interface import Interface
from recursos.Pessoas import Pessoas
from recursos.Estoque import Estoque


class PDV(Interface):
    cliente: str | None
    produtos: list
    valor_total: float
    cod_compra = 0

    def sair(self):
        self.input_com_decoracao(
            "PDV finalizado. Pressione qualquer tecla para continuar."
        )

    def compra(self):
        cliente = self.informar_cliente()
        if cliente == "SAIR":
            self.sair()
            return

        print(cliente)

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
            return None

        cliente = Pessoas.encontrar_cpf(cpf)

        if cliente == None:
            cont_op = self.input_com_decoracao(
                "Cadastro não encontrado! Faça cadastro no menu correspondente.\n    Deseja continuar com a compra sem cadastro? [S/N]"
            )

            while not Validacao.bool(cont_op):
                cont_op = self.input_com_decoracao(
                    "Resposta inválida. Deseja continuar com a compra sem cadastro? [S/N]"
                )

            if cont_op.upper() == "S":
                return None
            else:
                return "SAIR"

    def acrescentar_produto(self):
        cod_prod = self.input_com_decoracao("Digite o código do produto: ")

        while not Validacao.int(cod_prod):
            cod_prod = self.input_com_decoracao(
                "Código inválido - deve ser um número inteiro.\nDigite novamente o código do produto: "
            )

        prod = Estoque.encontrar_produto(cod_prod)

        if prod == None:
            cont_op = self.input_com_decoracao(
                "Produto não encontrado. Deseja tentar novamente? [S/N]"
            )

            while not Validacao.bool(cont_op):
                cont_op = self.input_com_decoracao(
                    "Resposta inválida. Deseja tentar novamente? [S/N]"
                )

            if cont_op.upper() == "S":
                return None
            else:
                return "VOLTAR"

        qtd = self.input_com_decoracao(
            f"Produto selecionado: {prod.get_nome()}\nDigite a quantidade desejada:"
        )

        # while not Validacao.int()

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

    def listar_carrinho(self):
        texto = "\n"

        return texto.join(
            [f"{x.get('qtd')} x {x.get('produto').get_nome()}" for x in self.produtos]
        )
