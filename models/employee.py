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
        self.registration = registration
        self.full_name = full_name
        self.cpf = cpf
        self.birth_date = birth_date
        self.department = department
        self.position = position
        self.salary = salary
        self.active = active

    def to_dict(self):
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
        pass  # You can implement this later if needed

    def deactivate(self):
        self.active = False

    def activate(self) -> None:
        self.active = True

    def __str__(self):
        status = "Active" if self.active else "Inactive"
        return (
            f"\nRegistration:\t{self.registration}\n"
            f"Name:\t\t{self.full_name}\n"
            f"CPF:\t\t{mask_cpf(self.cpf)}\n"
            f"Department:\t{self.department}\n"
            f"Position:\t{self.position}\n"
            f"Birth Date:\t{mask_date(self.birth_date.strftime('%d%m%Y'))}\n"
            f"Salary:\t\t{format_brl_currency(self.salary)}\n"
            f"Status:\t\t{status}"
        )
