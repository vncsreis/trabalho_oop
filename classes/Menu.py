class Menu:
    opcoes: list

    def __init__(self, opcoes):
        self.opcoes = opcoes

    def clear(self):
        print("\033c\033[3J", end="")

    def compor_ops(self):
        return "\n".join(f"{i + 1} - {x}" for i, x in enumerate(self.opcoes))

    def validar_op(self, op):
        if op.isnumeric():
            op_int = int(op)
            if op_int < 1 or op_int > len(self.opcoes):
                return False
            else:
                return True
        return False

    def detectar_op(self):
        string = self.compor_ops()
        self.clear()
        op = input(f"Selecione uma das opções:\n" + string + "\n")

        while not self.validar_op(op):
            self.clear()
            op = input(
                f"Seleção inválida.\nSelecione uma das opções:\n" + string + "\n"
            )
