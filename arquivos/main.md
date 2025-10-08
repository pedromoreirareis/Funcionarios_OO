# =============================================================================
# 🔧 Imports
# ============================================================================
import os
import csv
import json
import logging
import locale
from datetime import datetime
from pathlib import Path
from collections import namedtuple


# =============================================================================
# 🔧 Configurações de Arquivos e Diretórios
# =============================================================================

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

# --------------------------------------------------------------------------
#     # 🔧 VARIAVEIS GLOBAL
# --------------------------------------------------------------------------

#   Armazena o mior número da matricula
max_matricula = 1

# =============================================================================
# 🔧 Configuração de Logging
# =============================================================================

#   Configura sistema de log
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


# =============================================================================
# 🔧 Estruturas de Dados
# =============================================================================

#   Lista com os nome dos campos de um funcionário
CAMPOS_FUNCIONARIO = [
    "matricula",
    "nome_completo",
    "cpf",
    "dt_nasc",
    "dpto_empresa",
    "cargo",
    "salario",
    "ativo",
]

#   Gerador de tuplas nomeadas do tipo funcionario
Funcionario = namedtuple("Funcionario", CAMPOS_FUNCIONARIO)


# ==============================================================================
# 🔧 Funções Auxiliares
# ==============================================================================


def limpar_tela():
    """
    Limpa terminal | windows e linux
    """
    os.system("cls" if os.name == "nt" else "clear")


def pausar(mensagem="\n⏯️   Pressione ENTER para continuar..."):
    """
    Pausa programa para exebição de mensagem e avisos, aguarda ENTER
    """

    input(cor_texto(f"\n{mensagem}", "amarelo"))


def divisor_tela(
    caractere="=", largura=60, linha_antes=False, linha_depois=False
):
    """
    Imprime linha divisoria na tela - organizar a interface

    Parâmetros:
        caractere:  caracter a ser repedito
        largura: numero de vezes caracter sera repedito, padrao =60
        linha_antes: Se True
    """

    if linha_antes:
        print()

    print(caractere * largura)

    if linha_depois:
        print()


def cor_texto(texto, cor):

    CORES = {
        "reset": "\033[0m",
        "preto": "\033[30m",
        "vermelho": "\033[31m",
        "verde": "\033[32m",
        "amarelo": "\033[33m",
    }

    get_cor = CORES.get(cor)

    if get_cor:

        return f"{get_cor}{texto}{CORES['reset']}"
    else:

        return texto


def titulo(texto):

    divisor_tela(caractere="=", linha_antes=True)
    print(cor_texto(texto.upper().center(60), "amarelo"))
    divisor_tela(caractere="=", linha_depois=True)


def somente_digitos(digitos):

    return "".join(ch for ch in digitos if ch.isdigit())


def validar_cpf(cpf):

    if not cpf.isdigit():
        return False

    cpf_limpo = somente_digitos(cpf)

    if len(cpf_limpo) != 11:
        return False

    if cpf_limpo == cpf_limpo[0] * 11:
        return False

    return True


def validar_nome(nome):

    nome = nome.strip()

    if not isinstance(nome, str):
        return False

    if len(nome) < 3:
        return False

    if not all(ch.isalpha() or ch.isspace() for ch in nome):
        return False

    return True


def validar_dpto_cargo(dpto_cargo):

    dpto_cargo = dpto_cargo.strip()

    if not isinstance(dpto_cargo, str):
        return False

    if len(dpto_cargo) < 3:
        return False

    return True


def mascara_cpf(cpf):

    cpf = somente_digitos(cpf).zfill(11)

    return f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}"


def mascara_data(data):

    data = somente_digitos(data)

    return f"{data[0:2]}/{data[2:4]}/{data[4:8]}"


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


def f_exibir_func(titulo, dados):

    print(cor_texto(titulo, "amarelo") + cor_texto(dados, "verde"))


def resposta_positiva(valor):

    return valor.lower() in ["s", "sim", "y", "yes", "1", "true", "ativo"]


def resposta_negativa(valor):

    return valor.lower() in ["n", "nao", "não", "no", "0", "false", "inativo"]


def msg_print(texto, cor="amarelo"):

    print(cor_texto(texto, cor=cor))


# ==============================================================================
# 📦 Funções de Importação e Exportação
# ==============================================================================


def exibir_funcionario(func):

    f_exibir_func("\nMatrícula:\t", func.matricula)
    f_exibir_func("Nome:\t\t", func.nome_completo)
    f_exibir_func("CPF:\t\t", mascara_cpf(func.cpf))
    f_exibir_func("Departamento:\t", func.dpto_empresa)
    f_exibir_func("Cargo:\t\t", func.cargo)
    f_exibir_func("D. Nasc:\t", data_time_str(func.dt_nasc))
    f_exibir_func("Salário:\t", moeda_br(func.salario))

    if func.ativo:
        status = "Ativo"
    else:
        status = "Inativo"

    f_exibir_func("Status:\t\t", status)
    divisor_tela("-", largura=30)


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


def exportar_funcionarios(db_func, status=None):

    titulo(f"💾 Exportando dados para arquivo JSON.")
    print(
        cor_texto(
            f"\n📝  Exportando dados para {ARQUIVO_JSON.name}...", "amarelo"
        )
    )
    divisor_tela("-", linha_depois=True)

    registrar_log(
        LOG_EXPORTAR,
        mensagem=f"Iniciando Exportação para {ARQUIVO_JSON.name}",
    )

    try:

        with open(ARQUIVO_JSON, "w", encoding="utf-8") as arquivo:
            json.dump(
                preparar_exportar_json(db_func),
                arquivo,
                ensure_ascii=False,
                indent=4,
            )

        if status == 1:
            msg_print("\n✅  Funcionário cadastrado com sucesso!", "verde")

        if status == 0:
            msg_print(f"\n✅  Funcionário excluido com sucesso!", "verde")

        if status == None:
            msg_print(
                f"\n✅  {len(db_func)} funcionários exportados com sucesso!",
                "verde",
            )

        divisor_tela("=")

        registrar_log(
            LOG_EXPORTAR,
            mensagem=f"{len(db_func)} funcionários exportados com sucesso.",
        )

        pausar()

    except FileNotFoundError:

        registrar_log(
            LOG_EXPORTAR,
            mensagem="Arquivo ou diretório não encontrado.",
        )

    except PermissionError:

        registrar_log(
            LOG_EXPORTAR,
            mensagem="Permissão negada para escrever o arquivo.",
        )

    except TypeError:

        registrar_log(
            LOG_EXPORTAR,
            mensagem="Erro de serialização JSON.",
        )

    except OSError:

        registrar_log(
            LOG_EXPORTAR,
            mensagem="Erro de I/O ao gravar arquivo JSON.",
        )


def importar_csv(db_func):

    msg_print(f"\n⏳  Importando dados do arquivo {ARQUIVO_CSV.name}")
    divisor_tela(caractere="-")

    registrar_log(
        LOG_IMPORTAR_C,
        mensagem=f"Iniciando importação do arquivo {ARQUIVO_CSV.name}",
    )

    global max_matricula

    quant_func_import = 0

    try:

        with open(ARQUIVO_CSV, "r", encoding="utf-8") as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)

            for linha in leitor_csv:

                try:
                    matricula = int(linha["matricula"].strip())
                    nome_completo = linha["nome_completo"].strip()
                    cpf = linha["cpf"].strip()
                    dt_nasc = data_str_time(linha["dt_nasc"].strip())
                    dpto_empresa = linha["dpto_empresa"].strip()
                    cargo = linha["cargo"].strip()
                    salario = float(linha["salario"].strip())
                    ativo = linha["ativo"].lower() == "true"

                    funcionario = Funcionario(
                        matricula,
                        nome_completo,
                        cpf,
                        dt_nasc,
                        dpto_empresa,
                        cargo,
                        salario,
                        ativo,
                    )

                    db_func[funcionario.matricula] = funcionario

                    if matricula > max_matricula:
                        max_matricula = matricula

                    quant_func_import += 1

                except ValueError:

                    msg_print(
                        f"\n⁉️⚠️  Erro de conversão de dados para matrícula: {linha.get('matricula')}"
                    )

                    registrar_log(
                        LOG_IMPORTAR_C,
                        mensagem="Erro de conversão de tipos (ValueError)",
                    )

                    divisor_tela("X")

                except KeyError as e:

                    msg_print(f"\n⁉️⚠️  Campo ausente no CSV: {e}")

                    registrar_log(
                        LOG_IMPORTAR_C,
                        mensagem="Campo ausente no CSV (KeyError)",
                    )

                    divisor_tela("X")

            msg_print(
                f"\n✅  {quant_func_import} funcionários carregados do CSV!",
                "verde",
            )

            divisor_tela("=")

            registrar_log(
                LOG_IMPORTAR_C,
                f"{quant_func_import} funcionários importados com sucesso",
            )

    except FileNotFoundError:

        msg_print(
            f"\n⁉️⚠️  Erro: arquivo CSV não encontrado! Arquivo: '{ARQUIVO_CSV}'",
            "vermelho",
        )

        registrar_log(
            LOG_IMPORTAR_C,
            mensagem=f"Arquivo CSV não encontrado! Arquivo: '{ARQUIVO_CSV}'",
        )

    except Exception:

        msg_print(
            "\n⁉️⚠️🚨  Ocorreu um erro inesperado ao importar o CSV.", "vermelho"
        )
        registrar_log(LOG_IMPORTAR_C, mensagem="Erro inesperado (Exception)")

    exportar_funcionarios(db_func)


def importar_json(db_func):

    msg_print(f"\n📄 Importando dados do arquivo {ARQUIVO_JSON.name}...")
    divisor_tela("-", linha_depois=True)

    registrar_log(
        LOG_IMPORTAR_J,
        mensagem=f"Iniciando importação do arquivo {ARQUIVO_JSON.name}",
    )

    global max_matricula
    quant_func_import = 0

    try:

        with open(ARQUIVO_JSON, "r", encoding="utf-8") as arquivo_json:

            dados_json = json.load(arquivo_json)

            try:
                for matricula, dados_funcionario in dados_json.items():

                    funcionario = Funcionario(
                        int(dados_funcionario["matricula"]),
                        dados_funcionario["nome_completo"],
                        dados_funcionario["cpf"],
                        data_str_time(
                            dados_funcionario["dt_nasc"]
                        ),  # str -> datetime
                        dados_funcionario["dpto_empresa"],
                        dados_funcionario["cargo"],
                        float(dados_funcionario["salario"]),
                        bool(dados_funcionario["ativo"]),
                    )

                    db_func[funcionario.matricula] = funcionario

                    if funcionario.matricula > max_matricula:
                        max_matricula = funcionario.matricula

                    quant_func_import += 1

            except ValueError as e:

                msg_print(
                    f"\n⁉️⚠️  Erro de conversão de dados para matrícula {matricula}: {e}"
                )
                registrar_log(
                    LOG_IMPORTAR_J,
                    mensagem=f"\n⁉️⚠️ Erro de conversão de tipos para matrícula {matricula}",
                )

                divisor_tela("X")

            except KeyError as e:

                msg_print(
                    f"\n⁉️⚠️  Campo ausente para matrícula {matricula}: {e}"
                )
                registrar_log(
                    LOG_IMPORTAR_J,
                    mensagem=f"Campo ausente para matrícula {matricula}",
                )
                divisor_tela("X")

        msg_print(
            f"✅ {quant_func_import} funcionários importados do arquivo {ARQUIVO_JSON.name}",
            "verde",
        )

        divisor_tela("=")

        registrar_log(
            LOG_IMPORTAR_J,
            f"{quant_func_import} funcionários importados com sucesso",
        )

    except FileNotFoundError as e:
        msg_print(
            f"\n❌  Arquivo: {ARQUIVO_JSON.name} não encontrado.", "vermelho"
        )
        registrar_log(
            LOG_IMPORTAR_J,
            mensagem=f"Arquivo {ARQUIVO_JSON.name} não encontrado",
        )

    except json.JSONDecodeError as e:
        msg_print(
            f"\n❌  Erro ao decodificar JSON:  Arquivo: {ARQUIVO_JSON.name}",
            "vermelho",
        )
        registrar_log(LOG_IMPORTAR_J, mensagem="Erro de decodificação JSON")

    except Exception as e:
        msg_print(
            f"\n⁉️⚠️🚨  Ocorreu um erro inesperado ao importar {ARQUIVO_JSON.name}.",
            "vermelho",
        )
        registrar_log(LOG_IMPORTAR_J, mensagem="Erro inesperado (Exception)")


def exibir_funcionario_consulta(func, campos_extras):

    # campos obrigatorio -> matricula / nome / cpf

    f_exibir_func("\nMatrícula:\t", func.matricula)
    f_exibir_func("Nome:\t\t", func.nome_completo)
    f_exibir_func("CPF:\t\t", mascara_cpf(func.cpf))

    if campos_extras:
        for campo_extra in campos_extras:
            if campo_extra == "dt_nasc":
                f_exibir_func("D. Nasc:\t", data_time_str(func.dt_nasc))
            if campo_extra == "dpto_empresa":
                f_exibir_func("Departamento:\t", func.dpto_empresa)
            if campo_extra == "cargo":
                f_exibir_func("Cargo:\t\t", func.cargo)
            if campo_extra == "salario":
                f_exibir_func("Salário:\t", moeda_br(func.salario))
            if campo_extra == "ativo":
                if func.ativo:
                    status = "Ativo"
                else:
                    status = "Inativo"
                f_exibir_func("Status:\t\t", status)


def identificar_campo(entrada_usuario: str) -> str:

    mapa_campos = {
        "dpto_empresa": [
            "dpto_empresa",
            "departamento",
            "departamento_empresa",
            "depart",
            "dpto",
            "dep",
            "setor",
            "área",
            "area",
            "secao",
            "seção",
            "divisão",
            "divisao",
            "local",
            "local trabalho",
        ],
        "cargo": [
            "cargo",
            "funcao",
            "função",
            "funcao",
            "funçao",
            "ocupacao",
            "ocupação",
            "trabalho",
            "posto",
            "posição",
            "posicao",
            "tarefa",
            "atividade",
        ],
        "dt_nasc": [
            "dt_nasc",
            "nasc",
            "nascimento",
            "data nascimento",
            "ano nascimento",
            "dt_nascimento",
            "data",
            "ano",
            "data de nascimento",
            "dn",
        ],
        "ativo": [
            "ativo",
            "status",
            "trabalhando",
            "empregado",
            "situação",
            "situacao",
            "condição",
            "condicao",
            "em atividade",
            "inativo",
        ],
        "salario": [
            "salario",
            "salário",
            "remuneracao",
            "remuneração",
            "renda",
            "vencimento",
            "ganho",
            "pagamento",
            "piso salarial",
            "faixa salarial",
            "valor",
            "quantia",
        ],
    }

    entrada = entrada_usuario.strip().lower()  # normaliza
    for campo, sinonimos in mapa_campos.items():
        if entrada in [s.lower() for s in sinonimos]:
            return campo
    return ""


# ==============================================================================
# 🔧 Funções CRUD
# ==============================================================================


def inserir_funcionario(db_func):

    def titulo_inserir():
        limpar_tela()
        titulo(f"➕ Cadastrar novo funcionário.")

    def msg_entrada_invalida(msg):
        print(cor_texto(msg, "amarelo"))
        pausar()

    titulo_inserir()

    registrar_log(
        LOG_INSERIR,
        mensagem=f"Iniciando cadastro de novo funcionário",
    )

    #   Nome
    while True:
        titulo_inserir()

        nome = input("Nome completo: ").strip()

        if not (nome and validar_nome(nome)):
            msg_entrada_invalida("\nNome inválido.\n")
            continue
        break

    #   CPF
    while True:

        titulo_inserir()
        cpf = somente_digitos(input("CPF 11 Digitos: ").strip())

        if not validar_cpf(cpf):
            msg_entrada_invalida("\nCPF inválido.\n")
            continue

        if any(f.cpf == cpf for f in db_func.values()):
            print(cor_texto("\nCPF já cadastrado. ", "vermelho"))
            print(cor_texto("\nVoltando a tela inicial. ", "amarelo"))
            divisor_tela()
            registrar_log(
                LOG_INSERIR,
                f"Nome: {nome} - CPF: {cpf}",
                f"cadastro cancelado - CPF: {cpf} - já cadastrado",
            )
            pausar()
            return
        break

    #   Data Nascimento
    while True:
        titulo_inserir()

        try:
            dta_nasc = data_str_time(
                mascara_data(input("Nascimento (ddmmaaaa): ").strip())
            )
            break
        except Exception:
            print(cor_texto("\nData inválida", "amarelo"))
            pausar()

    #   Departamento
    while True:
        titulo_inserir()
        dpto = input("Departamento: ").strip() or "Geral"
        if not validar_dpto_cargo(dpto):
            msg_entrada_invalida("\nNome departamento inválido.\n")
            continue
        break

    #   Cargo
    while True:
        titulo_inserir()
        cargo = input("Cargo: ") or "Técnico"
        if not validar_dpto_cargo(cargo):
            msg_entrada_invalida("\nNome cargo inválido.\n")
            continue
        break

    #   Salario
    while True:
        titulo_inserir()
        salario_str = (
            input("Salário (ex: 1234,56): ")
            .strip()
            .replace(".", "")
            .replace(",", ".")
        )
        try:
            salario = float(salario_str)
            if salario < 0:
                print(
                    cor_texto("⚠️  O salário não pode ser negativo.", "amarelo")
                )
                pausar()
                continue
            break
        except Exception:
            print(cor_texto("Valor inválido", "amarelo"))
            pausar()

    #   Ativo
    while True:
        titulo_inserir()

        ativo = input("Ativo? (s/n) [s, sim,true]: ").strip().lower()

        if resposta_positiva(ativo):
            ativo = True
            break
        if resposta_negativa(ativo):
            ativo = False
            break

        else:
            msg_print(
                "\n\n⚠️   Entrada inválida. Por favor, responda com 's' ou 'n'."
            )
            pausar()
            continue

    #   matricula
    global max_matricula
    matricula = max_matricula + 1

    funcionario = Funcionario(
        matricula, nome, cpf, dta_nasc, dpto, cargo, salario, ativo
    )

    db_func[matricula] = funcionario
    max_matricula = funcionario.matricula

    limpar_tela()
    titulo_inserir()
    exibir_funcionario(funcionario)

    exportar_funcionarios(db_func, 1)

    registrar_log(
        LOG_INSERIR,
        preparar_funcionario_log(funcionario),
        "funcionário adicionado com sucesso",
    )


def apagar_funcionario(db_func):

    registrar_log(
        LOG_APAGAR, mensagem="Iniciando exclusão logica de funcionários..."
    )

    limpar_tela()
    titulo("🗑️  DESATIVAR FUNCIONÁRIOS")

    if not db_func:
        msg_print("\n❌   Nenhum funcionário cadastrado!!!", "vermelho")
        registrar_log(LOG_APAGAR, mensagem="Nenhum funcionário cadastrado!!!")
        pausar()
        return

    while True:
        limpar_tela()
        titulo("🗑️  DESATIVAR FUNCIONÁRIOS")

        matricula = input(cor_texto("Digite a matricula: ", "amarelo"))

        if not matricula.isdigit():
            msg_print("\nMatricula inválida. Digite novamente.", "vermelho")
            pausar()
            limpar_tela()
            continue
        break

    matricula = int(matricula)

    func = db_func.get(matricula)

    if not func:
        msg_print("\nMatricula não encontrada.")
        registrar_log(
            "apagar_funcionario",
            mensagem="Funcionário não cadastrado",
        )
        pausar()
        return
    if not func.ativo:

        msg_print(
            f"\nFuncionario(a):\n\n\t{func.nome_completo} de matricula {func.matricula} "
        )
        msg_print(f"\n\tEstá INATIVO", "vermelho")
        registrar_log(
            LOG_APAGAR,
            mensagem="Funcionário já excluido",
        )
        pausar()
        return

    exibir_funcionario(func)

    resposta = input(
        f"{cor_texto('\n🤔 Tem certeza que deseja excluir? ','amarelo')} {cor_texto(func.nome_completo,'verde')} ? [s/n]  "
    )

    if resposta_positiva(resposta):

        func_a_excluir = func._replace(ativo=False)
        db_func[matricula] = func_a_excluir

        limpar_tela()
        titulo("🗑️  DESATIVAR FUNCIONÁRIOS")

        exportar_funcionarios(db_func, 0)
        registrar_log(
            LOG_APAGAR,
            preparar_funcionario_log(func_a_excluir),
            mensagem="Exclusão logica de funcionários efetuada com sucesso...",
        )

        limpar_tela()
        titulo("🗑️  DESATIVAR FUNCIONÁRIOS")

        msg_print(f"Matricula funcionário excluido: {matricula}")
        exibir_funcionario(db_func.get(matricula))
        msg_print(
            f"\nFuncionário(a) {db_func.get(matricula).nome_completo} excluido com sucesso!",
            "verde",
        )
        divisor_tela("=")
        pausar()

    else:
        msg_print(
            f"\nExclusão do(a) funcionário(a) {db_func.get(matricula).nome_completo} cancelada",
            "vermelho",
        )
        divisor_tela("=")
        pausar()


def consultar_funcionarios(db_func):

    registrar_log(LOG_CONSULTAR, mensagem="iniando consulta de funcionários")

    limpar_tela()
    titulo("🔎  CONSULTAR FUNCIONÁRIOS ")

    if not db_func:
        msg_print("\n❌   Nenhum funcionário cadastrado!!!", "vermelho")
        registrar_log(
            LOG_CONSULTAR, mensagem="Nenhum funcionário cadastrado!!!"
        )
        pausar()
        return

    while True:
        limpar_tela()
        titulo("🔎  CONSULTAR FUNCIONÁRIOS ")

        print("1.  Nome")
        print("2.  CPF")
        print("3.  Matricula")
        print("0.  Voltar")

        divisor_tela("=")
        op = input("👉  Digite o critério de busca.....: ").strip()

        if op == "0":
            return

        if op not in ["1", "2", "3"]:
            msg_print("\n\nOpção inválida.")
            pausar()
            continue

        if op == "1":
            termo_buscado = input(
                f"\n👉  Digite o {cor_texto('nome',"verde")} para buscar......: "
            )
        elif op == "2":
            termo_buscado = input(
                f"\n👉  Digite o {cor_texto('CPF',"verde")} para buscar.......: "
            )
        elif op == "3":
            termo_buscado = input(
                f"\n👉  Digite a {cor_texto('matrícula',"verde")} para buscar.: "
            )

        # Nome
        if op == "1":
            termo_nome_normalizado = remover_acentos(termo_buscado).lower()
            resultados = [
                f
                for f in db_func.values()
                if termo_nome_normalizado
                in remover_acentos(f.nome_completo).lower()
            ]

        # CPF
        elif op == "2":
            termo_cpf = somente_digitos(termo_buscado)
            resultados = [
                f
                for f in db_func.values()
                if termo_cpf in somente_digitos(f.cpf)
            ]

        #   Matricula
        else:
            termo_matricula = somente_digitos(termo_buscado)
            resultados = [
                f
                for f in db_func.values()
                if termo_matricula in str(f.matricula)
            ]

        if not resultados:
            msg_print("\n🔍 ❌  Sem resultados.", "vermelho")
            registrar_log(LOG_CONSULTAR, f"termo = {termo_buscado}")
            pausar()
            return

        # Filtros Dinamicos
        divisor_tela("-", linha_antes=True)
        msg_print("\nFiltros extras? campo=valor (ENTER para pular)")

        while True:

            while True:

                msg_print(
                    "\nEx.: ano nascimento | departamento |  cargo   | ativo"
                )

                chave_filtro = input(">  ").strip().lower()

                chave_filtro = identificar_campo(chave_filtro)

                print(chave_filtro)

                if chave_filtro == "":
                    msg_print(
                        "\nℹ️❗ Nenhum filtro selecionado!!!\n", "vermelho"
                    )

                    break

                elif chave_filtro not in [
                    "dt_nasc",
                    "dpto_empresa",
                    "cargo",
                    "ativo",
                ]:
                    msg_print("\n\nOpção inválida.", "vermelho")
                    pausar()
                    continue
                break

            if chave_filtro != "":
                while True:

                    msg_print(
                        "\nPara: ano nascimento | departamento |  cargo   | ativo",
                        "vermelho",
                    )
                    msg_print(
                        f"Ex..:    1992        |  Comercial   | Analista |  true "
                    )
                    valor_filtro = input(">  ").strip()
                    if len(valor_filtro) < 2:
                        msg_print("\n\nOpção inválida.", "vermelho")
                        pausar()
                        continue
                    break

                msg_print(
                    f"\nFiltro extra de busca: {chave_filtro} > {valor_filtro}"
                )
                pausar()

                if chave_filtro not in CAMPOS_FUNCIONARIO:
                    msg_print("Campo inválido.")
                    continue

                valor_normalizado = valor_filtro.lower()

                def campo_valor(funcionario, chave_filtro):
                    valor_filtro = getattr(funcionario, chave_filtro)

                    if chave_filtro == "dt_nasc":
                        return data_time_str(valor_filtro).lower()
                    if chave_filtro == "ativo":
                        return "ativo" if valor_filtro else "inativo"
                    return str(valor_filtro).lower()

                resultados = [
                    f
                    for f in resultados
                    if valor_normalizado in campo_valor(f, chave_filtro)
                ]
                if not resultados:
                    break

            divisor_tela("-", linha_antes=True)
            campos_extras_possiveis = [
                campos_extras
                for campos_extras in CAMPOS_FUNCIONARIO
                if campos_extras not in ("matricula", "nome_completo", "cpf")
            ]
            msg_print(
                f"\nExtras ( , - virgula) ou ENTER: {','.join(campos_extras_possiveis)}"
            )

            campos_extras_solicitados = input("> ").strip()

            if campos_extras_solicitados == "":
                msg_print("\nℹ️❗ Nenhum campo extra será exibido", "vermelho")
                msg_print(
                    "\nℹ️❗ Sera exibido: Matricula, Nome, CPF.\n", "verde"
                )

            lista_campos_solicitados = [
                campos for campos in campos_extras_solicitados.split(",")
            ]

            lista_campos_solicitados_identificado = [
                identificar_campo(campos) for campos in lista_campos_solicitados
            ]

            campos_extras = (
                [
                    extra.strip()
                    for extra in lista_campos_solicitados_identificado
                    if extra in campos_extras_possiveis
                ]
                if campos_extras_solicitados
                else []
            )

            # Ordena por nome
            resultados.sort(
                key=lambda f: remover_acentos(f.nome_completo).lower()
            )

            break

        divisor_tela("-", linha_antes=True, linha_depois=True)
        msg_print("🔎 RESULTADOS: \n")

        for funcionario in resultados:
            exibir_funcionario_consulta(funcionario, campos_extras)

        resultdos_log = [
            [func.matricula, func.nome_completo] for func in resultados
        ]
        registrar_log(
            LOG_CONSULTAR,
            resultdos_log,
            f"termo_buscado='{termo_buscado}', nresultados = '{len(resultados)}' - sucesso",
        )
        pausar()


def listar_funcionarios(db_func):

    registrar_log(LOG_LISTAR, mensagem="Iniciando listagem de funcionários...")

    if not db_func:
        limpar_tela()
        titulo("📋  LISTAGEM FUNCIONÁRIOS")

        msg_print("\n\n❌   Nenhum funcionário cadastrado!!!", "vermelho")
        registrar_log(LOG_LISTAR, mensagem="Nenhum funcionário cadastrado!!!")
        pausar()

        return

    while True:

        limpar_tela()
        titulo("📋  LISTAGEM FUNCIONÁRIOS")

        print("1. Ativos\n2. Inativos\n3. Todos\n0. Voltar ao menu principal")

        divisor_tela("=", linha_antes=True)
        op = input("👉  Escolha uma opção: ").strip()

        if op == "1":
            filtro = "ativos"
        elif op == "2":
            filtro = "inativos"
        elif op == "3":
            filtro = "todos"
        elif op == "0":
            return
        else:
            print(f"\n⚠️  {cor_texto(' Atenção:','amarelo')} Opção inválida.\n")
            pausar()
            continue

        # Não tinha pensado sobre se a lista crescer muito, que vou percorrer a lista duas vezes

        if filtro == "ativos":

            func_filtrados = [func for func in db_func.values() if func.ativo]
            func_filtrados.sort(key=lambda f: remover_acentos(f.nome_completo))

            registrar_log(
                LOG_LISTAR,
                mensagem=f"Listagem {len(func_filtrados)} de funcionários ativos.",
            )

        elif filtro == "inativos":

            func_filtrados = [
                func for func in db_func.values() if not func.ativo
            ]
            func_filtrados.sort(key=lambda f: remover_acentos(f.nome_completo))
            registrar_log(
                LOG_LISTAR,
                mensagem=f"Listagem {len(func_filtrados)} de funcionários inativos.",
            )
        else:

            func_filtrados = sorted(
                db_func.values(),
                key=lambda f: (
                    not f.ativo,
                    remover_acentos(f.nome_completo),
                ),
            )

            registrar_log(
                LOG_LISTAR,
                mensagem=f"Listagem todos funcionários. Total: {len(func_filtrados)} ",
            )

        def list_quant(dict_func):
            msg_print(
                f"\n📋  Lista de Funcionários. {len(dict_func)} funcionários listados.",
                "verde",
            )

        list_quant(func_filtrados)

        divisor_tela("-", linha_depois=True)

        for func in func_filtrados:

            exibir_funcionario(func)

        list_quant(func_filtrados)

        pausar()


def calcular_folha(db_func):

    limpar_tela()
    titulo("💰  FOLHA DE PAGAMENTO")

    registrar_log(
        LOG_FOLHA,
        "Iniciando folha de pagamento",
    )

    if not db_func:

        divisor_tela(linha_antes=True)
        msg_print("\n📄 Calculando folha de pagamento...")
        divisor_tela("-")

        msg_print("\n\n❌   Nenhum funcionário cadastrado!!!", "vermelho")
        msg_print("\n⚠️   Não foi possível calcular folha de sálario.")

        registrar_log(LOG_FOLHA, mensagem="Nenhum funcionário cadastrado!!!")
        pausar()

        return

    divisor_tela(linha_antes=True)
    msg_print("\n📄 Calculando folha de pagamento...")
    divisor_tela("-")

    func_ativos = [func.salario for func in db_func.values() if func.ativo]

    valor_folha = sum(func_ativos)

    msg_print(
        f"\n✅  Folha de pagamento de {datetime.now().strftime("%B")} calculada com sucesso!",
        "verde",
    )

    divisor_tela("-")

    msg_print(
        f"\n👷  Total de funcionários:\t{len(func_ativos)} funcionários.",
        "verde",
    )
    msg_print(
        f"\n💰  Folha de pagamento:\t\t{moeda_br(valor_folha)}  💵", "verde"
    )

    divisor_tela("=")

    lista_folha_log = [
        [func.matricula, func.nome_completo, func.salario]
        for func in db_func.values()
        if func.ativo
    ]
    registrar_log(
        LOG_FOLHA,
        str(lista_folha_log),
        "Folha de salário calculada com sucesso",
    )

    pausar()


# =============================================================================
# 🚀 Carregamento do main
# =============================================================================


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


def carregar_dados(db_Funcionarios):

    registrar_log(
        LOG_CARREGAR, mensagem="Iniciando verificação de arquivos de dados."
    )

    # Verifica se o arquivo existe e se não está vazio
    if (
        ARQUIVO_JSON.exists()
        and ARQUIVO_JSON.is_file()
        and ARQUIVO_JSON.stat().st_size > 0
    ):

        msg_print(f"\n📄 Arquivo '{ARQUIVO_JSON.name}' encontrado...", "verde")
        divisor_tela(caractere="-")

        registrar_log(
            LOG_CARREGAR,
            mensagem=f"{ARQUIVO_JSON.name} encontrado. Solicitando importação",
        )

        importar_json(db_Funcionarios)

    else:

        msg_print(
            f"\n📄  Arquivo '{ARQUIVO_JSON.name}' não encontrado.", "vermelho"
        )
        msg_print(f"\n📄  Tentando importar o arquivo {ARQUIVO_CSV.name}.")

        registrar_log(
            LOG_CARREGAR,
            mensagem="Arquivo JSON não encontrado. Tentando importar do CSV inicial",
        )

        # Verifica se o arquivo CSV existe e se não está vazio
        if (
            ARQUIVO_CSV.exists()
            and ARQUIVO_CSV.is_file()
            and ARQUIVO_CSV.stat().st_size > 0
        ):
            # Existe e tem dados | Importar dados do CSV
            registrar_log(
                LOG_CARREGAR,
                mensagem=f"Arquivo {ARQUIVO_CSV.name} encontrado. Solicitando importação do CSV",
            )
            importar_csv(db_Funcionarios)

        else:  # Não existe ou não tem dados

            msg_print(
                f"\n⚠️  ATENÇÃO:\n('{ARQUIVO_JSON.name}' e \n'{ARQUIVO_CSV.name}\n')  não encontrados!",
                "vermelho",
            )
            msg_print("\n💻   O sistema iniciará sem dados carregados.")

            registrar_log(
                LOG_CARREGAR,
                f"Arquivo JSON e CSV não encontrados. Criando arquivo JSON {ARQUIVO_JSON.name}",
            )

            # Cria arquivo JSON vazio
            with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
                json.dump({}, f)

                registrar_log(
                    acao="criar_arquivo",
                    mensagem=f"Arquivo {ARQUIVO_JSON.name} vazio criado para iniciar o sistema.",
                )


# =============================================================================
# 🚀 Fluxo Principal e interface com usuário
# =============================================================================


def menu():

    limpar_tela()
    titulo("📋  MENU PRINCIPAL")
    print("Informe a opção desejada:")
    print("\n\t1. Inserir Funcionários")
    print("\t2. Listar Funcionários")
    print("\t3. Apagar Funcionários")
    print("\t4. Consultar Funcionários")
    print("\t5. Calcular folha de pagamento")
    print("\t6. Exportar funcionários")
    print("\t0. Sair\n")
    divisor_tela()

    try:
        op = int(input("👉  Digite o número da opção:   ").strip())
        print()
        return op

    except ValueError:
        return -1


# =============================================================================
# 🚀 Main
# =============================================================================


def main():
    #   Pedro Moreira

    limpar_tela()
    # --------------------------------------------------------------------------
    #     # 🔧 CONFIGURAR LOCALE
    # --------------------------------------------------------------------------

    configurar_locale()

    # --------------------------------------------------------------------------
    #     # 🔧 Iniciando
    # --------------------------------------------------------------------------

    # Saudação inicial e Log de inicialização do sistema
    print("\n\n## 🚀 Iniciando Sistema de Gestão de Funcionários ##\n")
    registrar_log(
        LOG_INICIAR, "sistema", mensagem="Sistema iniciado com sucesso."
    )

    # --------------------------------------------------------------------------
    #     # 🔧 VARIAVEIS GLOBAL
    # --------------------------------------------------------------------------

    Funcionarios = {}

    # --------------------------------------------------------------------------
    #     # 🔧 CARREGAMENTO INICIAL DE DADOS
    # --------------------------------------------------------------------------

    print("\n🔄  Carregando dados...".center(50))
    divisor_tela(caractere="-")

    carregar_dados(Funcionarios)
    pausar()

    # --------------------------------------------------------------------------
    #     # 🔧 INICIALIZANDO MENU
    # --------------------------------------------------------------------------

    opcao = -1

    while opcao != 0:
        opcao = menu()

        match opcao:
            case 1:
                limpar_tela()
                inserir_funcionario(Funcionarios)

            case 2:
                limpar_tela()
                listar_funcionarios(Funcionarios)
            case 3:
                limpar_tela()
                apagar_funcionario(Funcionarios)
            case 4:
                limpar_tela()
                consultar_funcionarios(Funcionarios)
            case 5:
                limpar_tela()
                calcular_folha(Funcionarios)
            case 6:
                limpar_tela()
                exportar_funcionarios(Funcionarios)
            case 0:
                limpar_tela()
                break
            case _:
                print(
                    f"\n⚠️  {cor_texto(' Atenção:','amarelo')} Opção digitada não está no menu.\n"
                )
                pausar()

    print("\n\n\t🛑🚪 Programa encerrado !!! 🚪🛑\n")
    registrar_log(
        LOG_FIM, "sistema", mensagem="Sistema encerrado pelo usuário."
    )
    pausar()


if __name__ == "__main__":
    main()
