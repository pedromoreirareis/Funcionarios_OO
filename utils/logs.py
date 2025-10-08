from utils import log_constants, paths
import logging
import json

# Configurações básicas do logger
logging.basicConfig(
    filename=paths.LOG_FILE,  # Caminho do arquivo onde os logs serão salvos
    level=logging.INFO,  # Nível mínimo de log: INFO registra eventos informativos e superiores
    datefmt=log_constants.LOG_DATE_FORMAT,  # Formato da data/hora exibida no log
    format=log_constants.LOG_FORMATTER,  # Formato da mensagem de log
    filemode="a",  # Modo de escrita: 'a' adiciona ao final, 'w' sobrescreve o arquivo
    encoding="utf-8",  # Codificação para suportar caracteres especiais
)

# Instância global do logger configurado
employee_logger = logging.getLogger()


def log_event(action, detail=None, message=None):
    """
    Registra uma mensagem formatada no arquivo de log.

    Args:
        action (str): Tipo de evento executado.
        detail (any): Dados extras relacionados ao evento.
        message (str): Descrição do que está acontecendo.

    Returns:
        bool: True se o log foi registrado com sucesso.
    """
    # Monta a mensagem de log conforme o tipo de ação
    if action == log_constants.LOG_INSERT:
        # Para inserção, serializa os detalhes como JSON
        msg = f"{action} - {json.dumps(detail, ensure_ascii=False)} - {message}"
    elif action in [
        log_constants.LOG_DELETE,
        log_constants.LOG_SEARCH,
        log_constants.LOG_PAYROLL,
    ]:
        # Para ações específicas, inclui detalhes e mensagem
        msg = f"{action} - {detail} - {message}"
    elif message:
        # Se houver apenas mensagem, inclui junto à ação
        msg = f"{action} - {message}"
    else:
        # Caso não haja detalhes nem mensagem, registra apenas a ação
        msg = action

    # Escreve a mensagem no arquivo de log
    return employee_logger.info(msg)
