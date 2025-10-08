from interface import screen


def main_menu():
    """
    Exibe o menu principal e retorna a opção escolhida.

    Returns:
        int: Número da opção escolhida ou -1 se inválida.
    """
    screen.clear_screen()
    screen.show_header("📋  MAIN MENU")

    print("Informe a opção desejada:")
    print("\n\t1. Adicionar Funcionário")
    print("\t2. Listar Funcionários")
    print("\t3. Remover Funcionário")
    print("\t4. Consultar Funcionários")
    print("\t5. Calcular Folha de Pagamento")
    print("\t6. Exportar Funcionários")
    print("\t0. Sair\n")

    screen.draw_divider()

    try:
        option = int(input("👉  Digite o número da opção:   ").strip())
        print()
        return option
    except ValueError:
        return -1
