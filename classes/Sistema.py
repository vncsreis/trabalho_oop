from classes.PDV import PDV
from classes.Menu import Menu


class Sistema:
    pdv: PDV
    menu: Menu

    def __init__(self):
        self.pdv = PDV()
        self.menu = Menu(["PDV", "Estoque", "Cadastro"])

    def run(self):
        while True:
            selec = self.menu.detectar_op()
            if selec == 1:
                self.pdv.compra()
