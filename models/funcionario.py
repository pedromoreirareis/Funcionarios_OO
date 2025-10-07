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

    def to_dict(self):
        return {
            "matricula": self.matricula,
            "nome_completo": self.nome_completo,
            "cpf": self.cpf,
            "dt_nasc": self.dt_nasc.strftime("%d/%m/%Y"),
            "dpto_empresa": self.dpto_empresa,
            "cargo": self.cargo,
            "salario": self.salario,
            "ativo": self.ativo,
        }

    def from_dict(self):
        pass

    def desativar_funcionario(self):
        self.ativo = False

    def ativar_funcionario(self) -> None:
        self.ativo = True

    def __str__(self):

        from utils.mascaras import mascara_cpf, mascara_data
        from utils.formatadores import moeda_br

        status = "Ativo" if self.ativo else "Inativo"
        return (
            f"\nMatrícula:\t{self.matricula}\n"
            f"Nome:\t\t{self.nome_completo}\n"
            f"CPF:\t\t{mascara_cpf(self.cpf)}\n"
            f"Departamento:\t{self.dpto_empresa}\n"
            f"Cargo:\t\t{self.cargo}\n"
            f"D. Nasc:\t{mascara_data(self.dt_nasc.strftime('%d%m%Y'))}\n"
            f"Salário:\t{moeda_br(self.salario)}\n"
            f"Status:\t\t{status}"
        )
