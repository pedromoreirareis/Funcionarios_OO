#   Diretorio base  (onde esta main.py)
DIRETORIO_BASE = Path(__file__).resolve().parent

#   Subdiretorio de dados dentro Diretório base
DIRETORIO_DADOS = DIRETORIO_BASE / "dados"

#   Se diretorio de 'dados' não existe, cria diretorio
DIRETORIO_DADOS.mkdir(exist_ok=True)

#   Caminho dos arquivos de persistência e log
ARQUIVO_CSV = DIRETORIO_DADOS / "funcionarios.csv"
ARQUIVO_JSON = DIRETORIO_DADOS / "funcionarios.json"
ARQUIVO_LOGS = DIRETORIO_DADOS / "logs.txt"

#   Formato mensagem dos logs
LOGS_FORMATTER = "[ %(asctime)s ] - %(message)s"

#   Formato data/hora logs
LOGS_DATE_FORMAT = "%d-%m-%Y %H:%M:%S"

#   Constantes para ações de logs
LOG_INSERIR = "*INSERIR*"
LOG_LISTAR = "*LISTAR*"
LOG_APAGAR = "*APAGAR*"
LOG_CONSULTAR = "*CONSULTAR*"
LOG_FOLHA = "*FOLHA_PG*"
LOG_EXPORTAR = "*EXPORTAR*"
LOG_IMPORTAR_J = "*IMPORTAR_JSON*"
LOG_IMPORTAR_C = "*IMPORTAR_CSV*"

LOG_INICIAR = "*INICIALIZOU*"
LOG_FIM = "*ENCERRANDO*"
LOG_LOCALE = "*LOCALE*"
LOG_CARREGAR = "*CARREGAR*"
LOG_CRIAR_J = "*CRIAR_JSON*"
LOG_CRIAR_C = "*CRIAR_CSV*"


def configurar_locale():

    registrar_log(
        LOG_LOCALE,
        mensagem="Iniciando configuração de Locale:pt_BR.UTF-8",
    )

    try:
        # Definindo o locale para o formato de moeda brasileiro
        locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
        registrar_log(
            LOG_LOCALE,
            mensagem="Locale:pt_BR.UTF-8 configurado com sucesso.",
        )

    except locale.Error:

        # Se não conseguiu "pt_BR.UTF-8", tenta o padrão do sistema
        locale.setlocale(locale.LC_ALL, "Portuguese_Brazil.1252")

        msg_print(
            "⚠️   Locale 'pt_BR.UTF-8' não está disponível no sistema.",
            "vermelho",
        )

        registrar_log(
            LOG_LOCALE,
            mensagem="Locale 'pt_BR.UTF-8' não está disponível no sistema.",
        )
