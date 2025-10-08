import locale
import unicodedata
from datetime import datetime


def remove_accents(text: str) -> str:

    if not isinstance(text, str):
        text = str(text)

    decomposed_text = unicodedata.normalize("NFD", text)
    without_accents = "".join(
        ch for ch in decomposed_text if not unicodedata.combining(ch)
    )
    return without_accents


def digits_only(value: str) -> str:
    return "".join(ch for ch in value if ch.isdigit())


def format_brl_currency(value: float) -> str:
    """
    Formata um valor float como moeda brasileira (R$).

    Args:
        value (float): Valor numérico a ser formatado.

    Returns:
        str: Valor formatado como string no padrão monetário brasileiro.
    """
    try:
        # Tenta formatar usando o locale atual do sistema
        return locale.currency(value, grouping=True)
    except Exception:
        # Fallback manual caso o locale não esteja configurado corretamente
        formatted = (
            f"{value:,.2f}".replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
        )
        return f"R$ {formatted}"


def str_to_date(date_str: str) -> datetime:
    """
    Converte uma string de data (dd/mm/yyyy) para um objeto datetime.

    Args:
        date_str (str): Data no formato dd/mm/yyyy.

    Returns:
        datetime: Objeto datetime correspondente à data fornecida.
    """
    return datetime.strptime(date_str, "%d/%m/%Y")


def date_to_str(date_timestamp: datetime) -> str:
    """
    Converte um objeto datetime para uma string no formato dd/mm/yyyy.

    Args:
        date_timestamp (datetime): Objeto datetime a ser convertido.

    Returns:
        str: Data formatada como string dd/mm/yyyy.
    """
    return datetime.strftime(date_timestamp, "%d/%m/%Y")


def today_str() -> str:
    """
    Retorna a data atual como string no formato dd/mm/yyyy.

    Returns:
        str: Data atual formatada como string dd/mm/yyyy.
    """
    # Usa datetime.today() para obter a data atual
    return datetime.today().strftime("%d/%m/%Y")


def format_cpf(cpf: str) -> str:
    """
    Formata uma string numérica como CPF (###.###.###-##).

    Args:
        cpf (str): CPF com ou sem pontuação.

    Returns:
        str: CPF formatado.
    """
    # Remove caracteres não numéricos e garante 11 dígitos
    cpf = digits_only(cpf).zfill(11)
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"


def format_date_br(date: str) -> str:
    """
    Formata uma string numérica como data (dd/mm/yyyy).

    Args:
        date (str): Data com ou sem separadores.

    Returns:
        str: Data formatada.
    """
    # Remove caracteres não numéricos
    date = digits_only(date)
    return f"{date[0:2]}/{date[2:4]}/{date[4:8]}"
