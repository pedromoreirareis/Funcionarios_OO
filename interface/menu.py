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
