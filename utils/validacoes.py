def validar_cpf(cpf):

    if not cpf.isdigit():
        return False

    cpf_limpo = somente_digitos(cpf)

    if len(cpf_limpo) != 11:
        return False

    if cpf_limpo == cpf_limpo[0] * 11:
        return False

    return True


def validar_nome(nome):

    nome = nome.strip()

    if not isinstance(nome, str):
        return False

    if len(nome) < 3:
        return False

    if not all(ch.isalpha() or ch.isspace() for ch in nome):
        return False

    return True


def validar_dpto_cargo(dpto_cargo):

    dpto_cargo = dpto_cargo.strip()

    if not isinstance(dpto_cargo, str):
        return False

    if len(dpto_cargo) < 3:
        return False

    return True


def resposta_positiva(valor):

    return valor.lower() in ["s", "sim", "y", "yes", "1", "true", "ativo"]


def resposta_negativa(valor):

    return valor.lower() in ["n", "nao", "não", "no", "0", "false", "inativo"]
