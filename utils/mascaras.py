def somente_digitos(digitos: str) -> str:

    return "".join(ch for ch in digitos if ch.isdigit())


def cpf(cpf: str) -> str:

    cpf = somente_digitos(cpf).zfill(11)

    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"


def mascara_data(data):

    data = somente_digitos(data)

    return f"{data[0:2]}/{data[2:4]}/{data[4:8]}"
