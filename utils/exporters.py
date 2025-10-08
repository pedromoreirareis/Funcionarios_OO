from utils import date_to_str


def prepare_employee_log(employee):
    """
    Prepara os dados de um funcionário para registro em log.

    Args:
        employee: Objeto nomeado (namedtuple ou similar) representando um funcionário.

    Returns:
        dict: Dicionário contendo os dados do funcionário com a data formatada.
    """
    employee_log = {}

    # Converte o objeto para dicionário
    employee_dict = employee._asdict()

    # Usa o número de registro como chave principal
    registration = employee_dict["registration"]

    # Formata a data de nascimento como string
    employee_dict["birth_date"] = date_to_str(employee_dict["birth_date"])

    # Adiciona ao log
    employee_log[registration] = employee_dict

    return employee_log


def prepare_json_export(employee_dict_group):
    """
    Prepara os dados de múltiplos funcionários para exportação em JSON.

    Args:
        employee_dict_group (dict): Dicionário contendo objetos nomeados de funcionários, indexados por número de registro.

    Returns:
        dict: Dicionário com os dados formatados para exportação, incluindo data de nascimento como string.
    """
    employee_json = {}

    # Itera sobre o dicionário de funcionários, onde cada chave é o número de registro
    for registration, employee in employee_dict_group.items():

        # Converte o objeto nomeado (namedtuple) para um dicionário
        employee_dict = employee._asdict()

        # Formata a data de nascimento como string no padrão dd/mm/yyyy
        employee_dict["birth_date"] = date_to_str(employee_dict["birth_date"])

        # Adiciona o dicionário formatado ao JSON final, usando o número de registro como chave
        employee_json[registration] = employee_dict

    # Retorna o dicionário completo com os dados formatados para exportação
    return employee_json
