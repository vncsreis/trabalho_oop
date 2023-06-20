class PDV:
    cliente: str
    produtos: list
    valor_total: float
    cod_compra = 0

    def compra(self):
        op_cpf = input("Possui cadastro conosco?")

    def imprimir_com_decoracao(self, texto):
        dec = f"""============================================
PDV
============================================
    {texto}
"""
