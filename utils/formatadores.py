def data_str_time(data_str):

    return datetime.strptime(data_str, "%d/%m/%Y")


def data_time_str(data_timestamp):

    return datetime.strftime(data_timestamp, "%d/%m/%Y")


def remover_acentos(texto):

    import unicodedata

    if not isinstance(texto, str):
        texto = str(texto)

    texto_decomposto = unicodedata.normalize("NFD", texto)
    sem_acentos = "".join(
        ch for ch in texto_decomposto if not unicodedata.combining(ch)
    )
    return sem_acentos


def moeda_br(valor):

    try:
        return locale.currency(valor, grouping=True)

    except Exception:

        moeda = (
            f"{valor:,.2f}".replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
        )

        return f"R$ {moeda}"


def preparar_funcionario_log(funcionario):

    func_para_log = {}

    func_dict = funcionario._asdict()
    matricula = func_dict["matricula"]
    func_dict["dt_nasc"] = data_time_str(func_dict["dt_nasc"])
    func_para_log[matricula] = func_dict

    return func_para_log


def preparar_exportar_json(func_tuple):

    func_para_json = {}

    for matricula, funcionario in func_tuple.items():

        func_dict = funcionario._asdict()
        func_dict["dt_nasc"] = data_time_str(func_dict["dt_nasc"])
        func_para_json[matricula] = func_dict

    return func_para_json
