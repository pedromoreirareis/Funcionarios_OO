from datetime import datetime
from utils.masks import mask_cpf, mask_date
from utils.currency_formatters import format_brl_currency


class Employee:
    def __init__(
        self,
        registration: int,
        full_name: str,
        cpf: str,
        birth_date: datetime,
        department: str,
        position: str,
        salary: float,
        active: bool,
    ):
        # Inicializa os atributos do funcionário
        self.registration = registration
        self.full_name = full_name
        self.cpf = cpf
        self.birth_date = birth_date
        self.department = department
        self.position = position
        self.salary = salary
        self.active = active

    def to_dict(self):
        """
        Retorna os dados do funcionário como um dicionário formatado.
        """
        return {
            "registration": self.registration,
            "full_name": self.full_name,
            "cpf": self.cpf,
            "birth_date": self.birth_date.strftime("%d/%m/%Y"),
            "department": self.department,
            "position": self.position,
            "salary": self.salary,
            "active": self.active,
        }

    def from_dict(self):
        """
        Método reservado para popular os dados do funcionário a partir de um dicionário.
        """
        pass  # Implementar se necessário

    def deactivate(self):
        """
        Marca o funcionário como inativo.
        """
        self.active = False

    def activate(self) -> None:
        """
        Marca o funcionário como ativo.
        """
        self.active = True
