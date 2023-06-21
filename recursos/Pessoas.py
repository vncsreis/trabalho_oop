from classes.Cliente import Cliente


class Pessoas:
    clientes = [
        Cliente("Roberto", 74203373069, 8810000, []),
        Cliente("João", 10964464055, 8810000, []),
        Cliente("Fabiana", 83976627070, 8810000, []),
    ]

    funcionarios = []

    def encontrar_cpf(cpf):
        pessoas = Pessoas.clientes + Pessoas.funcionarios

        for p in pessoas:
            if p.cpf == cpf:
                return p
        return None
