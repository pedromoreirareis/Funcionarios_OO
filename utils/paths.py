from pathlib import Path

#   Diretorio base  (onde esta main.py)
DIRETORIO_BASE = Path(__file__).resolve().parent

#   Subdiretorio de dados dentro Diretório base
DIRETORIO_DADOS = DIRETORIO_BASE / "data"

#   Se diretorio de 'dados' não existe, cria diretorio
DIRETORIO_DADOS.mkdir(exist_ok=True)

#   Caminho dos arquivos de persistência e log
ARQUIVO_CSV = DIRETORIO_DADOS / "funcionarios.csv"
ARQUIVO_JSON = DIRETORIO_DADOS / "funcionarios.json"
ARQUIVO_LOGS = DIRETORIO_DADOS / "logs.log"
