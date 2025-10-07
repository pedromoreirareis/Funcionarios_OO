import locale


def format_brl_currency(valor):

    try:
        return locale.currency(valor, grouping=True)

    except Exception:

        moeda = (
            f"{valor:,.2f}".replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
        )

        return f"R$ {moeda}"
