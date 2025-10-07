#   Formato mensagem dos logs
LOGS_FORMATTER = "[ %(asctime)s ] - %(message)s"

#   Formato data/hora logs
LOGS_DATE_FORMAT = "%d-%m-%Y %H:%M:%S"

#   Constantes para ações de logs
LOG_INSERT = "INSERIR"
LOG_LIST = "LISTAR"
LOG_DELETE = "APAGAR"
LOG_SERACH = "CONSULTAR"
LOG_PAYROOL = "FOLHA_PG"
LOG_EXPORT = "EXPORTAR"
LOG_IMPORT_JSON = "IMPORTAR_JSON"
LOG_IMPORT_CSV = "IMPORTAR_CSV"

LOG_START = "INICIALIZOU"
LOG_END = "ENCERRANDO"
LOG_LOCALE = "LOCALE"
LOG_LOAD = "CARREGAR"
LOG_CREATE_JSON = "CRIAR_JSON"
LOG_CREATE_CSV = "CRIAR_CSV"
LOG_UNKNOWN = "UNKNOWN"

LOG_MESSAGES_PT = {
    "INSERT": {
        "start": "🟡 Iniciando processo de inclusão.",
        "success": "✅ Funcionário incluído com sucesso.",
        "error": "❌ Erro ao incluir funcionário.",
        "empty": "📭 Nenhum dado para incluir.",
        "detail": lambda nome, matricula: f"✅ Funcionário '{nome}' incluído com matrícula {matricula}.",
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
        "detail": lambda nome, matricula: f"🗑️ Funcionário '{nome}' com matrícula {matricula} foi excluído.",
    },
    "SEARCH": {
        "start": "🟡 Iniciando consulta.",
        "success": "🔍 Consulta concluída.",
        "error": "❌ Erro na consulta.",
        "empty": "📭 Nenhum resultado encontrado.",
        "detail": lambda termo: f"🔎 Consulta realizada com o termo '{termo}'.",
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
    # 🔮 Genérico para ações futuras ou desconhecidas
    "UNKNOWN": {
        "start": "🟡 Ação desconhecida iniciada.",
        "success": "✅ Ação concluída.",
        "error": "❌ Erro em ação desconhecida.",
        "warning": "⚠️ Ação executada com ressalvas.",
    },
}


def get_log_message(code: str, status: str, **kwargs) -> str:
    """
    Retorna uma mensagem amigável em português com base no código e no tipo de evento do log.

    Parâmetros:
        code (str): Código do log (ex: "*INSERT*", "*SEARCH*").
        status (str): Tipo de evento (ex: "start", "success", "error").
        **kwargs: Parâmetros opcionais para mensagens dinâmicas.

    Retorna:
        str: Mensagem formatada para exibição ao usuário.
    """
    bloco = LOG_MESSAGES_PT.get(code, LOG_MESSAGES_PT["*UNKNOWN*"])
    mensagem = bloco.get(status)

    # Se a mensagem for uma função (como um lambda), executa com os parâmetros fornecidos
    if callable(mensagem):
        resultado = mensagem(**kwargs)
        return str(resultado) if resultado is not None else "ℹ️ Ação registrada."

    # Se for uma string comum, retorna diretamente
    return str(mensagem) if mensagem is not None else "ℹ️ Ação registrada."
