from classes.PDV import PDV
from classes.Estoque import Estoque
from classes.Menu import Menu


class Sistema:
    pdv: PDV
    estoque: Estoque
    menu: Menu

    def __init__(self):
        self.estoque = Estoque([])
        self.pdv = PDV()
        self.menu = Menu(["Teste 1", "Teste 2"])

    def run(self):
        selec = self.menu.detectar_op()
