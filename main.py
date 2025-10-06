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
