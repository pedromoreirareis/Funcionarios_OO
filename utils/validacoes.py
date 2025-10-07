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


def identificar_campo(entrada_usuario: str) -> str:

    mapa_campos = {
        "dpto_empresa": [
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
        "cargo": [
            "cargo",
            "funcao",
            "função",
            "funcao",
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
        "dt_nasc": [
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
        "ativo": [
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
        "salario": [
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

    entrada = entrada_usuario.strip().lower()  # normaliza
    for campo, sinonimos in mapa_campos.items():
        if entrada in [s.lower() for s in sinonimos]:
            return campo
    return ""
