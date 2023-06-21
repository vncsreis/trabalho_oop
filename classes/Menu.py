from classes.Interface import Interface
from classes.Validacao import Validacao


class Menu(Interface):
    opcoes: list

    def __init__(self, opcoes):
        self.opcoes = opcoes

    def compor_ops(self):
        return "\n".join(f"{i + 1} - {x}" for i, x in enumerate(self.opcoes))

    def detectar_op(self):
        string = self.compor_ops()
        self.clear()
        op = input(f"Selecione uma das opções:\n" + string + "\n")

        while not Validacao.op(op, self.opcoes):
            self.clear()
            op = input(
                f"Seleção inválida.\nSelecione uma das opções:\n" + string + "\n"
            )

        return int(op)
