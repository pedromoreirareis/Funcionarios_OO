import unicodedata


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
