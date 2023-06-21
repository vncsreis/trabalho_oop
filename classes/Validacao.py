from bradocs4py.cpf import validar_cpf


class Validacao:
    def op(op, opcoes):
        if op.isnumeric():
            op_int = int(op)
            if op_int < 1 or op_int > len(opcoes):
                return False
            else:
                return True
        return False

    def bool(op):
        if op.upper() not in ["S", "N"]:
            return False
        else:
            return True

    def cpf(cpf):
        return validar_cpf(cpf)

    def int(cod):
        return cod.isnumeric()
