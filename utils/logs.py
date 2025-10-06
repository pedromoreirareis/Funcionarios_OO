import logging


logging.basicConfig(
    filename=ARQUIVO_LOGS,  #   Arquivo onde logs serão salvos
    level=logging.INFO,  #   Nível minimo do log
    datefmt=LOGS_DATE_FORMAT,  #   Formato da data e hora
    format=LOGS_FORMATTER,  #   Formato do log
    filemode="w",  #   Modo abertura - 'w' - sobreescreve / 'a' - insere
    encoding="utf-8",  #   Encoding caracteres
)

#   Instancia do logger configurado
logger_msg_funcionario = logging.getLogger()


def registrar_log(acao, detalhe=None, mensagem=None):
    """
    Registra mensagem formatada no arquivo de log.

    Formatação de acordo com ação realizada.
    Args:
        acao:   tipo de evento executado
        detalhe:    dados extras
        mensagem:   descrição do que está acontecendo
    """

    if acao == LOG_INSERIR:

        msg = f"{acao} - {json.dumps(detalhe, ensure_ascii=False)} - {mensagem}"

    elif acao in [LOG_APAGAR, LOG_CONSULTAR, LOG_FOLHA]:

        msg = f"{acao} - {detalhe} - {mensagem}"

    elif mensagem:

        msg = f"{acao} - {mensagem}"

    else:

        msg = acao

    return logger_msg_funcionario.info(msg)
