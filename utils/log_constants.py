# Formato da mensagem dos logs
LOG_FORMATTER = "[ %(asctime)s ] - %(message)s"

# Formato da data/hora nos logs
LOG_DATE_FORMAT = "%d-%m-%Y %H:%M:%S"

# Constantes de ação para registro de logs CRUD
LOG_INSERT = "INSERT"
LOG_LIST = "LIST"
LOG_DELETE = "DELETE"
LOG_SEARCH = "SEARCH"
LOG_PAYROLL = "PAYROLL"
LOG_EXPORT = "EXPORT"
LOG_IMPORT_JSON = "IMPORT_JSON"
LOG_IMPORT_CSV = "IMPORT_CSV"

# Constantes de ação para registro de logs Eventos sistema
LOG_STARTUP = "STARTUP"
LOG_SHUTDOWN = "SHUTDOWN"
LOG_LOCALE = "LOCALE"
LOG_LOAD = "LOAD"
LOG_CREATE_JSON = "CREATE_JSON"
LOG_CREATE_CSV = "CREATE_CSV"
LOG_UNKNOWN = "UNKNOWN"

# Mensagens de log em português
LOG_MESSAGES_PT = {
    "INSERT": {
        "start": "🟡 Iniciando processo de inclusão.",
        "success": "✅ Funcionário incluído com sucesso.",
        "error": "❌ Erro ao incluir funcionário.",
        "empty": "📭 Nenhum dado para incluir.",
        "detail": lambda name, registration: f"✅ Funcionário '{name}' incluído com matrícula {registration}.",
    },
    "LIST": {
        "start": "🟡 Iniciando listagem.",
        "success": "📋 Lista exibida com sucesso.",
        "error": "❌ Erro ao listar dados.",
        "empty": "📭 Nenhum item encontrado.",
    },
    "DELETE": {
        "start": "🟡 Iniciando exclusão.",
        "success": "🗑️ Exclusão realizada com sucesso.",
        "error": "❌ Erro ao excluir item.",
        "detail": lambda name, registration: f"🗑️ Funcionário '{name}' com matrícula {registration} foi excluído.",
    },
    "SEARCH": {
        "start": "🟡 Iniciando consulta.",
        "success": "🔍 Consulta concluída.",
        "error": "❌ Erro na consulta.",
        "empty": "📭 Nenhum resultado encontrado.",
        "detail": lambda term: f"🔎 Consulta realizada com o termo '{term}'.",
    },
    "PAYROLL": {
        "start": "🟡 Gerando folha de pagamento.",
        "success": "💰 Folha gerada com sucesso.",
        "error": "❌ Erro ao gerar folha.",
    },
    "EXPORT": {
        "start": "🟡 Exportando dados.",
        "success": "📤 Exportação concluída.",
        "error": "❌ Erro na exportação.",
    },
    "IMPORT_JSON": {
        "start": "🟡 Importando JSON.",
        "success": "📥 JSON importado com sucesso.",
        "error": "❌ Erro ao importar JSON.",
    },
    "IMPORT_CSV": {
        "start": "🟡 Importando CSV.",
        "success": "📥 CSV importado com sucesso.",
        "error": "❌ Erro ao importar CSV.",
    },
    "STARTUP": {
        "start": "🚀 Sistema inicializado.",
    },
    "SHUTDOWN": {
        "start": "🛑 Sistema encerrado.",
    },
    "LOCALE": {
        "start": "🌐 Configurando locale.",
        "success": "🌐 Locale configurado com sucesso.",
        "error": "❌ Erro ao configurar locale.",
    },
    "LOAD": {
        "start": "🟡 Carregando dados.",
        "success": "📂 Dados carregados.",
        "error": "❌ Erro ao carregar dados.",
    },
    "CREATE_JSON": {
        "start": "🟡 Criando JSON.",
        "success": "📝 JSON criado.",
        "error": "❌ Erro ao criar JSON.",
    },
    "CREATE_CSV": {
        "start": "🟡 Criando CSV.",
        "success": "📝 CSV criado.",
        "error": "❌ Erro ao criar CSV.",
    },
    "UNKNOWN": {
        "start": "🟡 Ação desconhecida iniciada.",
        "success": "✅ Ação concluída.",
        "error": "❌ Erro em ação desconhecida.",
        "warning": "⚠️ Ação executada com ressalvas.",
    },
}


def get_log_message(code: str, status: str, **kwargs) -> str:
    """
    Retorna uma mensagem de log amigável em português.

    Args:
        code (str): Código da ação de log.
        status (str): Tipo de evento (start, success, error).
        **kwargs: Parâmetros opcionais para mensagens dinâmicas.

    Returns:
        str: Mensagem formatada para exibição.
    """
    block = LOG_MESSAGES_PT.get(code, LOG_MESSAGES_PT["UNKNOWN"])
    message = block.get(status)

    # Executa função lambda se necessário
    if callable(message):
        result = message(**kwargs)
        return str(result) if result is not None else "ℹ️ Ação registrada."

    # Retorna mensagem estática
    return str(message) if message is not None else "ℹ️ Ação registrada."
