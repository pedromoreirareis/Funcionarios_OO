from utils.text_formatters import digits_only


def mask_cpf(cpf: str) -> str:
    cpf = digits_only(cpf).zfill(11)
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"


def mask_date(date: str) -> str:
    date = digits_only(date)
    return f"{date[0:2]}/{date[2:4]}/{date[4:8]}"
