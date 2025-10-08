import os


def clear_screen():
    """
    Limpa o terminal (Windows ou Linux).
    """
    os.system("cls" if os.name == "nt" else "clear")


def pause(message="\n⏯️   Pressione ENTER para continuar..."):
    """
    Pausa o programa e aguarda ENTER.

    Args:
        message (str): Mensagem exibida ao usuário.
    """
    input(color_text(f"\n{message}", "yellow"))


def draw_divider(char="=", width=60, before=False, after=False):
    """
    Imprime uma linha divisória na tela.

    Args:
        char (str): Caractere repetido.
        width (int): Largura da linha.
        before (bool): Se True, pula linha antes.
        after (bool): Se True, pula linha depois.
    """
    if before:
        print()
    print(char * width)
    if after:
        print()


def color_text(text, color):
    """
    Aplica cor ANSI ao texto.

    Args:
        text (str): Texto a ser colorido.
        color (str): Nome da cor.

    Returns:
        str: Texto com código de cor ANSI.
    """
    COLORS = {
        "reset": "\033[0m",
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
    }

    selected_color = COLORS.get(color)
    return (
        f"{selected_color}{text}{COLORS['reset']}" if selected_color else text
    )


def show_header(text):
    """
    Exibe título centralizado com bordas.

    Args:
        text (str): Texto do título.
    """
    draw_divider(char="=", before=True)
    print(color_text(text.upper().center(60), "yellow"))
    draw_divider(char="=", after=True)


def show_field(label, value):
    """
    Exibe campo formatado com título e valor.
    Para exibição de listagem de funcionários

    Ex:->
    Nome:   Pedro Silva
    CPF:    123.456.789-00


    Args:
        label (str): Nome do campo.
        value (str): Valor do campo.
    """
    print(color_text(label, "yellow") + color_text(value, "green"))


def show_message(text, color="yellow"):
    """
    Exibe mensagem com cor definida.

    Args:
        text (str): Mensagem a ser exibida.
        color (str): Cor da mensagem.
    """
    print(color_text(text, color=color))
