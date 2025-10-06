from datetime import datetime


class Funcionario:
    def __init__(
        self,
        matricula: int,
        nome_completo: str,
        cpf: str,
        dt_nasc: datetime,
        dpto_empresa: str,
        cargo: str,
        salario: float,
        ativo: bool,
    ):

        self.matricula = matricula
        self.nome_completo = nome_completo
        self.cpf = cpf
        self.dt_nasc = dt_nasc
        self.dpto_empresa = dpto_empresa
        self.cargo = cargo
        self.salario = salario
        self.ativo = ativo

    def para_dict(self):
        return {
            "matricula": self.matricula,
            "nome_completo": self.nome_completo,
            "cpf": self.cpf,
            "dt_nasc": self.dt_nasc,
            "dpto_empresa": self.dpto_empresa,
            "cargo": self.cargo,
            "salario": self.salario,
            "ativo": self.ativo,
        }
