"""
Configura locale em padrão brasileiro - Locale:pt_BR.UTF-8
Caso não seja possível imprementa fallback em ambiente windows Portuguese_Brazil.1252

Locale utilizado para principalmente para tratamento de valores float, monetários e data.
"""

import locale
from utils import logs
from utils.log_constants import LOG_LOCALE


def configurar_locale():
    """
    Configura o locale da aplicação para o formato brasileiro.

    A função tenta definir o locale `pt_BR.UTF-8`. Caso não esteja disponível,
     aplica um fallback para `Portuguese_Brazil.1252`, comum em sistemas Windows.

    Durante o processo, mensagens de sucesso ou falha são registradas no log.

    Returns:
        bool:
            - `True` se o locale `pt_BR.UTF-8` foi configurado com sucesso.
            - `False` se foi necessário utilizar o fallback.

    Side Effects:
        - Altera a configuração global de locale da aplicação.
        - Registra mensagens no sistema de logs.

    Exemplos:
        >>> from utils.locale_config import configurar_locale
        >>> if not configurar_locale():
        ...     print("⚠️ Locale brasileiro não disponível, usando fallback.")
    """

    # Regitra log no inicio da configuração de locale
    logs.registrar_log(
        LOG_LOCALE,
        mensagem="Iniciando configuração de Locale:pt_BR.UTF-8",
    )

    try:
        # Tenta definir locale padrão Linux/Unix brasileiro
        locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

        # Se deu certo, registra log de sucesso
        logs.registrar_log(
            LOG_LOCALE,
            mensagem="Locale:pt_BR.UTF-8 configurado com sucesso.",
        )

        # Retorna True infromando que locale foi configurado com sucesso
        return True

    except locale.Error:

        # Caso não consiga "pt_BR.UTF-8", tenta fallback do windows
        locale.setlocale(
            locale.LC_ALL,
            "Portuguese_Brazil.1252",
        )

        # Registra log informando sque foi necessário fallback
        logs.registrar_log(
            LOG_LOCALE,
            mensagem="fallBack - Locale 'pt_BR.UTF-8' não está disponível no sistema.",
        )

        # Retorna False indicando que foi necessário falback
        return False
