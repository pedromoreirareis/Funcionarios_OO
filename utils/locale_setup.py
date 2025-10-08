import locale
from utils import logs
from utils import log_constants


def setup_locale() -> bool:
    """
    Configura o locale brasileiro com fallback para Windows.

    Returns:
        bool: True se configurado com sucesso, False se usou fallback.
    """
    # Registra log no início da configuração de locale
    logs.log_event(
        log_constants.LOG_LOCALE,
        message="Iniciando configuração de Locale:pt_BR.UTF-8",
    )

    try:
        # Tenta definir locale padrão Linux/Unix brasileiro
        locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

        # Registra log de sucesso
        logs.log_event(
            log_constants.LOG_LOCALE,
            message="Locale:pt_BR.UTF-8 configurado com sucesso.",
        )

        return True

    except locale.Error:
        # Fallback para locale do Windows
        locale.setlocale(locale.LC_ALL, "Portuguese_Brazil.1252")

        # Registra log informando que foi necessário fallback
        logs.log_event(
            log_constants.LOG_LOCALE,
            message="Fallback - Locale 'pt_BR.UTF-8' não está disponível no sistema.",
        )

        return False
