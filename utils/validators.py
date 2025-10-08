from utils.formatters import digits_only


def is_valid_cpf(cpf: str) -> bool:
    """
    Valida se o CPF é numérico e possui 11 dígitos.

    Args:
        cpf (str): CPF com ou sem pontuação.

    Returns:
        bool: True se válido, False se inválido.
    """
    if not cpf.isdigit():
        return False

    clean_cpf = digits_only(cpf)

    if len(clean_cpf) != 11:
        return False

    if clean_cpf == clean_cpf[0] * 11:
        return False

    return True


def is_valid_name(name: str) -> bool:
    """
    Valida se o nome é uma string com pelo menos 3 letras.

    Args:
        name (str): Nome completo.

    Returns:
        bool: True se válido, False se inválido.
    """
    name = name.strip()

    if not isinstance(name, str):
        return False

    if len(name) < 3:
        return False

    if not all(ch.isalpha() or ch.isspace() for ch in name):
        return False

    return True


def is_valid_role_or_department(value: str) -> bool:
    """
    Valida se o campo de cargo ou departamento é uma string com pelo menos 3 caracteres.

    Args:
        value (str): Nome do cargo ou departamento.

    Returns:
        bool: True se válido, False se inválido.
    """
    value = value.strip()

    if not isinstance(value, str):
        return False

    if len(value) < 3:
        return False

    return True


def is_affirmative(value: str) -> bool:
    """
    Verifica se o valor representa uma resposta positiva.

    Args:
        value (str): Texto da resposta.

    Returns:
        bool: True se afirmativa, False caso contrário.
    """
    return value.lower() in ["s", "sim", "y", "yes", "1", "true", "ativo"]


def is_negative(value: str) -> bool:
    """
    Verifica se o valor representa uma resposta negativa.

    Args:
        value (str): Texto da resposta.

    Returns:
        bool: True se negativa, False caso contrário.
    """
    return value.lower() in ["n", "nao", "não", "no", "0", "false", "inativo"]


def identify_field(user_input: str) -> str:
    """
    Identifica o campo correspondente com base em sinônimos.

    Args:
        user_input (str): Texto digitado pelo usuário.

    Returns:
        str: Nome do campo identificado ou string vazia.
    """
    field_map = {
        "department": [
            "dpto_empresa",
            "departamento",
            "departamento_empresa",
            "depart",
            "dpto",
            "dep",
            "setor",
            "área",
            "area",
            "secao",
            "seção",
            "divisão",
            "divisao",
            "local",
            "local trabalho",
        ],
        "role": [
            "cargo",
            "funcao",
            "função",
            "funçao",
            "ocupacao",
            "ocupação",
            "trabalho",
            "posto",
            "posição",
            "posicao",
            "tarefa",
            "atividade",
        ],
        "birth_date": [
            "dt_nasc",
            "nasc",
            "nascimento",
            "data nascimento",
            "ano nascimento",
            "dt_nascimento",
            "data",
            "ano",
            "data de nascimento",
            "dn",
        ],
        "active": [
            "ativo",
            "status",
            "trabalhando",
            "empregado",
            "situação",
            "situacao",
            "condição",
            "condicao",
            "em atividade",
            "inativo",
        ],
        "salary": [
            "salario",
            "salário",
            "remuneracao",
            "remuneração",
            "renda",
            "vencimento",
            "ganho",
            "pagamento",
            "piso salarial",
            "faixa salarial",
            "valor",
            "quantia",
        ],
    }

    normalized = user_input.strip().lower()

    for field, synonyms in field_map.items():
        if normalized in [s.lower() for s in synonyms]:
            return field

    return ""
