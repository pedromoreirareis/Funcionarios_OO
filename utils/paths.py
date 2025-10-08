from pathlib import Path

# Diretório base (onde está o main.py)
BASE_DIR = Path(__file__).resolve().parent

# Subdiretório de dados dentro do diretório base
DATA_DIR = BASE_DIR / "data"

# Se o diretório 'data' não existe, cria o diretório
DATA_DIR.mkdir(exist_ok=True)

# Caminhos dos arquivos de persistência e log
CSV_FILE = DATA_DIR / "employees.csv"
JSON_FILE = DATA_DIR / "employees.json"
LOG_FILE = DATA_DIR / "logs.log"
