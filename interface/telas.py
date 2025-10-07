import os


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


def f_exibir_func(titulo, dados):

    print(cor_texto(titulo, "amarelo") + cor_texto(dados, "verde"))


def msg_print(texto, cor="amarelo"):

    print(cor_texto(texto, cor=cor))
