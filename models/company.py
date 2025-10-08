class Company:
    def __init__(self) -> None:
        self.employees = {}  # Armazena funcionários por matrícula
        self.max_registration = 0  # Última matrícula registrada

    def add_employee(self, employee_data):
        """
        Adiciona um novo funcionário ao sistema.

        Args:
            employee_data: Dados do funcionário (não utilizados diretamente).
        Returns:
            None
        """
        def show_title():
            clear_screen()
            show_header("➕ Cadastrar novo funcionário.")

        def show_invalid_input(msg):
            print(color_text(msg, "yellow"))
            pause()

        show_title()

        log_event(LOG_INSERT, message="Iniciando cadastro de novo funcionário")

        # Nome
        while True:
            show_title()
            name = input("Nome completo: ").strip()
            if not (name and is_valid_name(name)):
                show_invalid_input("\nNome inválido.\n")
                continue
            break

        # CPF
        while True:
            show_title()
            cpf = digits_only(input("CPF 11 dígitos: ").strip())
            if not is_valid_cpf(cpf):
                show_invalid_input("\nCPF inválido.\n")
                continue
            if any(emp.cpf == cpf for emp in employee_db.values()):
                print(color_text("\nCPF já cadastrado.", "red"))
                print(color_text("\nVoltando à tela inicial.", "yellow"))
                draw_divider()
                log_event(LOG_INSERT, f"Nome: {name} - CPF: {cpf}", "Cadastro cancelado - CPF já cadastrado")
                pause()
                return
            break

        # Data de nascimento
        while True:
            show_title()
            try:
                birth_date = str_to_date(format_date(input("Nascimento (ddmmaaaa): ").strip()))
                break
            except Exception:
                print(color_text("\nData inválida", "yellow"))
                pause()

        # Departamento
        while True:
            show_title()
            department = input("Departamento: ").strip() or "Geral"
            if not is_valid_role_or_department(department):
                show_invalid_input("\nNome de departamento inválido.\n")
                continue
            break

        # Cargo
        while True:
            show_title()
            role = input("Cargo: ").strip() or "Técnico"
            if not is_valid_role_or_department(role):
                show_invalid_input("\nNome de cargo inválido.\n")
                continue
            break

        # Salário
        while True:
            show_title()
            salary_input = input("Salário (ex: 1234,56): ").strip().replace(".", "").replace(",", ".")
            try:
                salary = float(salary_input)
                if salary < 0:
                    print(color_text("⚠️  O salário não pode ser negativo.", "yellow"))
                    pause()
                    continue
                break
            except Exception:
                print(color_text("Valor inválido", "yellow"))
                pause()

        # Ativo
        while True:
            show_title()
            active_input = input("Ativo? (s/n) [s, sim, true]: ").strip().lower()
            if is_affirmative(active_input):
                active = True
                break
            if is_negative(active_input):
                active = False
                break
            show_message("\n⚠️ Entrada inválida. Responda com 's' ou 'n'.")
            pause()

        # Matrícula
        global max_registration
        registration = max_registration + 1

        employee = Employee(registration, name, cpf, birth_date, department, role, salary, active)
        employee_db[registration] = employee
        max_registration = employee.registration

        clear_screen()
        show_title()
        display_employee(employee)

        export_employees(employee_db, include_active=True)

        log_event(LOG_INSERT, prepare_employee_log(employee), "Funcionário adicionado com sucesso")

    def deactivate_employee(self, registration_input):
        """
        Desativa um funcionário com base na matrícula.

        Args:
            registration_input (str): Matrícula informada pelo usuário.
        Returns:
            None
        """
        log_event(LOG_DELETE, message="Iniciando exclusão lógica de funcionários...")
        clear_screen()
        show_header("🗑️  DESATIVAR FUNCIONÁRIOS")

        if not employee_db:
            show_message("\n❌ Nenhum funcionário cadastrado!", "red")
            log_event(LOG_DELETE, message="Nenhum funcionário cadastrado!")
            pause()
            return

        while True:
            clear_screen()
            show_header("🗑️  DESATIVAR FUNCIONÁRIOS")
            registration_input = input(color_text("Digite a matrícula: ", "yellow"))
            if not registration_input.isdigit():
                show_message("\nMatrícula inválida. Digite novamente.", "red")
                pause()
                continue
            break

        registration = int(registration_input)
        employee = employee_db.get(registration)

        if not employee:
            show_message("\nMatrícula não encontrada.")
            log_event("deactivate_employee", message="Funcionário não cadastrado")
            pause()
            return

        if not employee.active:
            show_message(f"\nFuncionário(a): {employee.full_name} de matrícula {employee.registration}")
            show_message("\n\tEstá INATIVO", "red")
            log_event(LOG_DELETE, message="Funcionário já excluído")
            pause()
            return

        display_employee(employee)

        confirm = input(f"{color_text('🤔 Tem certeza que deseja excluir? ', 'yellow')} {color_text(employee.full_name, 'green')} ? [s/n] ")

        if is_affirmative(confirm):
            updated_employee = employee._replace(active=False)
            employee_db[registration] = updated_employee

            clear_screen()
            show_header("🗑️  DESATIVAR FUNCIONÁRIOS")

            export_employees(employee_db, include_active=False)
            log_event(LOG_DELETE, prepare_employee_log(updated_employee), message="Exclusão lógica efetuada com sucesso")

            clear_screen()
            show_header("🗑️  DESATIVAR FUNCIONÁRIOS")
            show_message(f"Matrícula funcionário excluído: {registration}")
            display_employee(employee_db.get(registration))
            show_message(f"\nFuncionário(a) {employee_db.get(registration).full_name} excluído com sucesso!", "green")
            draw_divider("=")
            pause()
        else:
            show_message(f"\nExclusão de {employee_db.get(registration).full_name} cancelada", "red")
            draw_divider("=")
            pause()

    def search_employees(self):
        """
        Realiza consulta de funcionários por nome, CPF ou matrícula.

        Returns:
            None
        """
        log_event(LOG_SEARCH, message="Iniciando consulta de funcionários")
        clear_screen()
        show_header("🔎  CONSULTAR FUNCIONÁRIOS")

        if not employee_db:
            show_message("\n❌ Nenhum funcionário cadastrado!", "red")
            log_event(LOG_SEARCH, message="Nenhum funcionário cadastrado")
            pause()
            return

        while True:
            clear_screen()
            show_header("🔎  CONSULTAR FUNCIONÁRIOS")

            print("1.  Nome")
            print("2.  CPF")
            print("3.  Matrícula")
            print("0.  Voltar")

            draw_divider("=")
            option = input("👉  Digite o critério de busca.....: ").strip()

            if option == "0":
                return

            if option not in ["1", "2", "3"]:
                show_message("\n\nOpção inválida.")
                pause()
                continue

            if option == "1":
                search_term = input(f"\n👉  Digite o {color_text('nome', 'green')} para buscar......: ")
            elif option == "2":
                search_term = input(f"\n👉  Digite o {color_text('CPF', 'green')} para buscar.......: ")
            elif option == "3":
                search_term = input(f"\n👉  Digite a {color_text('matrícula', 'green')} para buscar.: ")

            # Busca por nome
            if option == "1":
                normalized_name = remove_accents(search_term).lower()
                results = [
                    emp for emp in employee_db.values()
                    if normalized_name in remove_accents(emp.full_name).lower()
                ]

            # Busca por CPF
            elif option == "2":
                normalized_cpf = digits_only(search_term)
                results = [
                    emp for emp in employee_db.values()
                    if normalized_cpf in digits_only(emp.cpf)
                ]

            # Busca por matrícula
            else:
                normalized_registration = digits_only(search_term)
                results = [
                    emp for emp in employee_db.values()
                    if normalized_registration in str(emp.registration)
                ]

            if not results:
                show_message("\n🔍 ❌  Sem resultados.", "red")
                log_event(LOG_SEARCH, f"search_term = {search_term}")
                pause()
                return

            # Filtros extras
            draw_divider("-", before=True)
            show_message("\nFiltros extras? campo=valor (ENTER para pular)")

            while True:
                while True:
                    show_message("\nEx.: ano nascimento | departamento | cargo | ativo")
                    filter_key = input("> ").strip().lower()
                    filter_key = identify_field(filter_key)

                    if filter_key == "":
                        show_message("\nℹ️❗ Nenhum filtro selecionado!\n", "red")
                        break

                    if filter_key not in ["birth_date", "department", "role", "active"]:
                        show_message("\n\nOpção inválida.", "red")
                        pause()
                        continue
                    break

                if filter_key != "":
                    while True:
                        show_message("\nPara: ano nascimento | departamento | cargo | ativo", "red")
                        show_message("Ex..: 1992 | Comercial | Analista | true")
                        filter_value = input("> ").strip()
                        if len(filter_value) < 2:
                            show_message("\n\nOpção inválida.", "red")
                            pause()
                            continue
                        break

                    show_message(f"\nFiltro extra de busca: {filter_key} > {filter_value}")
                    pause()

                    if filter_key not in EMPLOYEE_FIELDS:
                        show_message("Campo inválido.")
                        continue

                    normalized_value = filter_value.lower()

                    def get_field_value(employee, key):
                        value = getattr(employee, key)
                        if key == "birth_date":
                            return date_to_str(value).lower()
                        if key == "active":
                            return "ativo" if value else "inativo"
                        return str(value).lower()

                    results = [
                        emp for emp in results
                        if normalized_value in get_field_value(emp, filter_key)
                    ]
                    if not results:
                        break

                # Campos extras
                draw_divider("-", before=True)
                possible_extra_fields = [
                    field for field in EMPLOYEE_FIELDS
                    if field not in ("registration", "full_name", "cpf")
                ]
                show_message(f"\nExtras (separados por vírgula) ou ENTER: {','.join(possible_extra_fields)}")

                requested_fields = input("> ").strip()

                if requested_fields == "":
                    show_message("\nℹ️❗ Nenhum campo extra será exibido", "red")
                    show_message("\nℹ️❗ Será exibido: Matrícula, Nome, CPF.\n", "green")

                raw_fields = [field.strip() for field in requested_fields.split(",")]
                identified_fields = [identify_field(field) for field in raw_fields]

                extra_fields = [
                    field for field in identified_fields
                    if field in possible_extra_fields
                ] if requested_fields else []

                # Ordena por nome
                results.sort(key=lambda emp: remove_accents(emp.full_name).lower())

                break

            draw_divider("-", before=True, after=True)
            show_message("🔎 RESULTADOS: \n")

            for emp in results:
                display_employee_search(emp, extra_fields)

            log_summary = [[emp.registration, emp.full_name] for emp in results]
            log_event(
                LOG_SEARCH,
                log_summary,
                f"search_term='{search_term}', results='{len(results)}' - sucesso"
            )
            pause()


            registrar_log(
                LOG_CONSULTAR, mensagem="iniando consulta de funcionários"
            )

            limpar_tela()
            titulo("🔎  CONSULTAR FUNCIONÁRIOS ")

            if not db_func:
                msg_print("\n❌   Nenhum funcionário cadastrado!!!", "vermelho")
                registrar_log(
                    LOG_CONSULTAR, mensagem="Nenhum funcionário cadastrado!!!"
                )
                pausar()
                return

            while True:
                limpar_tela()
                titulo("🔎  CONSULTAR FUNCIONÁRIOS ")

                print("1.  Nome")
                print("2.  CPF")
                print("3.  Matricula")
                print("0.  Voltar")

                divisor_tela("=")
                op = input("👉  Digite o critério de busca.....: ").strip()

                if op == "0":
                    return

                if op not in ["1", "2", "3"]:
                    msg_print("\n\nOpção inválida.")
                    pausar()
                    continue

                if op == "1":
                    termo_buscado = input(
                        f"\n👉  Digite o {cor_texto('nome',"verde")} para buscar......: "
                    )
                elif op == "2":
                    termo_buscado = input(
                        f"\n👉  Digite o {cor_texto('CPF',"verde")} para buscar.......: "
                    )
                elif op == "3":
                    termo_buscado = input(
                        f"\n👉  Digite a {cor_texto('matrícula',"verde")} para buscar.: "
                    )

                # Nome
                if op == "1":
                    termo_nome_normalizado = remover_acentos(termo_buscado).lower()
                    resultados = [
                        f
                        for f in db_func.values()
                        if termo_nome_normalizado
                        in remover_acentos(f.nome_completo).lower()
                    ]

                # CPF
                elif op == "2":
                    termo_cpf = somente_digitos(termo_buscado)
                    resultados = [
                        f
                        for f in db_func.values()
                        if termo_cpf in somente_digitos(f.cpf)
                    ]

                #   Matricula
                else:
                    termo_matricula = somente_digitos(termo_buscado)
                    resultados = [
                        f
                        for f in db_func.values()
                        if termo_matricula in str(f.matricula)
                    ]

                if not resultados:
                    msg_print("\n🔍 ❌  Sem resultados.", "vermelho")
                    registrar_log(LOG_CONSULTAR, f"termo = {termo_buscado}")
                    pausar()
                    return

                # Filtros Dinamicos
                divisor_tela("-", linha_antes=True)
                msg_print("\nFiltros extras? campo=valor (ENTER para pular)")

                while True:

                    while True:

                        msg_print(
                            "\nEx.: ano nascimento | departamento |  cargo   | ativo"
                        )

                        chave_filtro = input(">  ").strip().lower()

                        chave_filtro = identificar_campo(chave_filtro)

                        print(chave_filtro)

                        if chave_filtro == "":
                            msg_print(
                                "\nℹ️❗ Nenhum filtro selecionado!!!\n", "vermelho"
                            )

                            break

                        elif chave_filtro not in [
                            "dt_nasc",
                            "dpto_empresa",
                            "cargo",
                            "ativo",
                        ]:
                            msg_print("\n\nOpção inválida.", "vermelho")
                            pausar()
                            continue
                        break

                    if chave_filtro != "":
                        while True:

                            msg_print(
                                "\nPara: ano nascimento | departamento |  cargo   | ativo",
                                "vermelho",
                            )
                            msg_print(
                                f"Ex..:    1992        |  Comercial   | Analista |  true "
                            )
                            valor_filtro = input(">  ").strip()
                            if len(valor_filtro) < 2:
                                msg_print("\n\nOpção inválida.", "vermelho")
                                pausar()
                                continue
                            break

                        msg_print(
                            f"\nFiltro extra de busca: {chave_filtro} > {valor_filtro}"
                        )
                        pausar()

                        if chave_filtro not in CAMPOS_FUNCIONARIO:
                            msg_print("Campo inválido.")
                            continue

                        valor_normalizado = valor_filtro.lower()

                        def campo_valor(funcionario, chave_filtro):
                            valor_filtro = getattr(funcionario, chave_filtro)

                            if chave_filtro == "dt_nasc":
                                return data_time_str(valor_filtro).lower()
                            if chave_filtro == "ativo":
                                return "ativo" if valor_filtro else "inativo"
                            return str(valor_filtro).lower()

                        resultados = [
                            f
                            for f in resultados
                            if valor_normalizado in campo_valor(f, chave_filtro)
                        ]
                        if not resultados:
                            break

                    divisor_tela("-", linha_antes=True)
                    campos_extras_possiveis = [
                        campos_extras
                        for campos_extras in CAMPOS_FUNCIONARIO
                        if campos_extras
                        not in ("matricula", "nome_completo", "cpf")
                    ]
                    msg_print(
                        f"\nExtras ( , - virgula) ou ENTER: {','.join(campos_extras_possiveis)}"
                    )

                    campos_extras_solicitados = input("> ").strip()

                    if campos_extras_solicitados == "":
                        msg_print(
                            "\nℹ️❗ Nenhum campo extra será exibido", "vermelho"
                        )
                        msg_print(
                            "\nℹ️❗ Sera exibido: Matricula, Nome, CPF.\n", "verde"
                        )

                    lista_campos_solicitados = [
                        campos for campos in campos_extras_solicitados.split(",")
                    ]

                    lista_campos_solicitados_identificado = [
                        identificar_campo(campos)
                        for campos in lista_campos_solicitados
                    ]

                    campos_extras = (
                        [
                            extra.strip()
                            for extra in lista_campos_solicitados_identificado
                            if extra in campos_extras_possiveis
                        ]
                        if campos_extras_solicitados
                        else []
                    )

                    # Ordena por nome
                    resultados.sort(
                        key=lambda f: remover_acentos(f.nome_completo).lower()
                    )

                    break

                divisor_tela("-", linha_antes=True, linha_depois=True)
                msg_print("🔎 RESULTADOS: \n")

                for funcionario in resultados:
                    exibir_funcionario_consulta(funcionario, campos_extras)

                resultdos_log = [
                    [func.matricula, func.nome_completo] for func in resultados
                ]
                registrar_log(
                    LOG_CONSULTAR,
                    resultdos_log,
                    f"termo_buscado='{termo_buscado}', nresultados = '{len(resultados)}' - sucesso",
                )
                pausar()

    def list_employees(self, status="all"):
        """
        Exibe lista de funcionários filtrando por status.

        Args:
            status (str): 'active', 'inactive' ou 'all'.

        Returns:
            None
        """
        log_event(LOG_LIST, message="Iniciando listagem de funcionários...")

        if not employee_db:
            clear_screen()
            show_header("📋  LISTAGEM FUNCIONÁRIOS")
            show_message("\n❌ Nenhum funcionário cadastrado!", "red")
            log_event(LOG_LIST, message="Nenhum funcionário cadastrado!")
            pause()
            return

        while True:
            clear_screen()
            show_header("📋  LISTAGEM FUNCIONÁRIOS")

            print("1. Ativos\n2. Inativos\n3. Todos\n0. Voltar ao menu principal")
            draw_divider("=", before=True)

            option = input("👉  Escolha uma opção: ").strip()

            if option == "1":
                filter_status = "active"
            elif option == "2":
                filter_status = "inactive"
            elif option == "3":
                filter_status = "all"
            elif option == "0":
                return
            else:
                print(f"\n⚠️  {color_text('Atenção:', 'yellow')} Opção inválida.\n")
                pause()
                continue

            # Filtra funcionários conforme o status selecionado
            if filter_status == "active":
                filtered_employees = [
                    emp for emp in employee_db.values() if emp.active
                ]
                filtered_employees.sort(key=lambda e: remove_accents(e.full_name))
                log_event(LOG_LIST, message=f"Listagem de {len(filtered_employees)} funcionários ativos.")

            elif filter_status == "inactive":
                filtered_employees = [
                    emp for emp in employee_db.values() if not emp.active
                ]
                filtered_employees.sort(key=lambda e: remove_accents(e.full_name))
                log_event(LOG_LIST, message=f"Listagem de {len(filtered_employees)} funcionários inativos.")

            else:
                filtered_employees = sorted(
                    employee_db.values(),
                    key=lambda e: (not e.active, remove_accents(e.full_name)),
                )
                log_event(LOG_LIST, message=f"Listagem de todos os funcionários. Total: {len(filtered_employees)}")

            def show_count(employee_list):
                show_message(
                    f"\n📋 Lista de Funcionários: {len(employee_list)} encontrados.",
                    "green",
                )

            show_count(filtered_employees)
            draw_divider("-", after=True)

            for emp in filtered_employees:
                display_employee(emp)

            show_count(filtered_employees)
            pause()

    def calculate_payroll(self):
        """
        Calcula o valor total da folha de pagamento dos funcionários ativos.

        Returns:
            None
        """
        clear_screen()
        show_header("💰  FOLHA DE PAGAMENTO")

        log_event(LOG_PAYROLL, "Iniciando folha de pagamento")

        if not employee_db:
            draw_divider(before=True)
            show_message("\n📄 Calculando folha de pagamento...")
            draw_divider("-")
            show_message("\n❌ Nenhum funcionário cadastrado!", "red")
            show_message("\n⚠️ Não foi possível calcular a folha.")
            log_event(LOG_PAYROLL, message="Nenhum funcionário cadastrado")
            pause()
            return

        draw_divider(before=True)
        show_message("\n📄 Calculando folha de pagamento...")
        draw_divider("-")

        active_salaries = [emp.salary for emp in employee_db.values() if emp.active]
        total_payroll = sum(active_salaries)

        show_message(
            f"\n✅ Folha de pagamento de {datetime.now().strftime('%B')} calculada com sucesso!",
            "green",
        )
        draw_divider("-")
        show_message(f"\n👷 Total de funcionários:\t{len(active_salaries)}", "green")
        show_message(f"\n💰 Valor total:\t\t{format_brl_currency(total_payroll)} 💵", "green")
        draw_divider("=")

        payroll_log = [
            [emp.registration, emp.full_name, emp.salary]
            for emp in employee_db.values()
            if emp.active
        ]
        log_event(LOG_PAYROLL, str(payroll_log), "Folha calculada com sucesso")
        pause()

    def import_csv(self, path):
        """
        Importa dados de funcionários a partir de um arquivo CSV.

        Args:
            path (str): Caminho do arquivo CSV.

        Returns:
            None
        """
        show_message(f"\n⏳ Importando dados do arquivo {CSV_FILE.name}")
        draw_divider("-")

        log_event(LOG_IMPORT_CSV, message=f"Iniciando importação do arquivo {CSV_FILE.name}")

        global max_registration
        imported_count = 0

        try:
            with open(CSV_FILE, "r", encoding="utf-8") as csv_file:
                reader = csv.DictReader(csv_file)

                for row in reader:
                    try:
                        registration = int(row["matricula"].strip())
                        full_name = row["nome_completo"].strip()
                        cpf = row["cpf"].strip()
                        birth_date = str_to_date(row["dt_nasc"].strip())
                        department = row["dpto_empresa"].strip()
                        role = row["cargo"].strip()
                        salary = float(row["salario"].strip())
                        active = row["ativo"].lower() == "true"

                        employee = Employee(
                            registration, full_name, cpf, birth_date,
                            department, role, salary, active
                        )

                        employee_db[employee.registration] = employee

                        if registration > max_registration:
                            max_registration = registration

                        imported_count += 1

                    except ValueError:
                        show_message(f"\n⁉️⚠️ Erro de conversão para matrícula: {row.get('matricula')}")
                        log_event(LOG_IMPORT_CSV, message="Erro de conversão de tipos (ValueError)")
                        draw_divider("X")

                    except KeyError as e:
                        show_message(f"\n⁉️⚠️ Campo ausente no CSV: {e}")
                        log_event(LOG_IMPORT_CSV, message="Campo ausente no CSV (KeyError)")
                        draw_divider("X")

            show_message(f"\n✅ {imported_count} funcionários carregados do CSV!", "green")
            draw_divider("=")
            log_event(LOG_IMPORT_CSV, f"{imported_count} funcionários importados com sucesso")

        except FileNotFoundError:
            show_message(f"\n⁉️⚠️ Arquivo CSV não encontrado: '{CSV_FILE}'", "red")
            log_event(LOG_IMPORT_CSV, message=f"Arquivo CSV não encontrado: '{CSV_FILE}'")

        except Exception:
            show_message("\n⁉️⚠️🚨 Erro inesperado ao importar o CSV.", "red")
            log_event(LOG_IMPORT_CSV, message="Erro inesperado (Exception)")

        export_employees(employee_db)

    def import_json(self, path):
        """
        Importa dados de funcionários a partir de um arquivo JSON.

        Args:
            path (str): Caminho do arquivo JSON.

        Returns:
            None
        """
        show_message(f"\n📄 Importando dados do arquivo {JSON_FILE.name}...")
        draw_divider("-", after=True)

        log_event(LOG_IMPORT_JSON, message=f"Iniciando importação do arquivo {JSON_FILE.name}")

        global max_registration
        imported_count = 0

        try:
            with open(JSON_FILE, "r", encoding="utf-8") as json_file:
                data = json.load(json_file)

                try:
                    for registration, emp_data in data.items():
                        employee = Employee(
                            int(emp_data["matricula"]),
                            emp_data["nome_completo"],
                            emp_data["cpf"],
                            str_to_date(emp_data["dt_nasc"]),
                            emp_data["dpto_empresa"],
                            emp_data["cargo"],
                            float(emp_data["salario"]),
                            bool(emp_data["ativo"]),
                        )

                        employee_db[employee.registration] = employee

                        if employee.registration > max_registration:
                            max_registration = employee.registration

                        imported_count += 1

                except ValueError as e:
                    show_message(f"\n⁉️⚠️ Erro de conversão para matrícula {registration}: {e}")
                    log_event(LOG_IMPORT_JSON, message=f"Erro de conversão para matrícula {registration}")
                    draw_divider("X")

                except KeyError as e:
                    show_message(f"\n⁉️⚠️ Campo ausente para matrícula {registration}: {e}")
                    log_event(LOG_IMPORT_JSON, message=f"Campo ausente para matrícula {registration}")
                    draw_divider("X")

            show_message(f"✅ {imported_count} funcionários importados do arquivo {JSON_FILE.name}", "green")
            draw_divider("=")
            log_event(LOG_IMPORT_JSON, f"{imported_count} funcionários importados com sucesso")

        except FileNotFoundError:
            show_message(f"\n❌ Arquivo {JSON_FILE.name} não encontrado.", "red")
            log_event(LOG_IMPORT_JSON, message=f"Arquivo {JSON_FILE.name} não encontrado")

        except json.JSONDecodeError:
            show_message(f"\n❌ Erro ao decodificar JSON: {JSON_FILE.name}", "red")
            log_event(LOG_IMPORT_JSON, message="Erro de decodificação JSON")

        except Exception:
            show_message(f"\n⁉️⚠️🚨 Erro inesperado ao importar {JSON_FILE.name}.", "red")
            log_event(LOG_IMPORT_JSON, message="Erro inesperado (Exception)")

    def export_employees(self, path, status=None):
        """
        Exporta os dados dos funcionários para arquivo JSON.

        Args:
            path (str): Caminho do arquivo.
            status (int | None): Define mensagem de sucesso (1=cadastro, 0=exclusão).

        Returns:
            None
        """
        show_header("💾 Exportando dados para arquivo JSON.")
        print(color_text(f"\n📝 Exportando dados para {JSON_FILE.name}...", "yellow"))
        draw_divider("-", after=True)

        log_event(LOG_EXPORT, message=f"Iniciando exportação para {JSON_FILE.name}")

        try:
            with open(JSON_FILE, "w", encoding="utf-8") as file:
                json.dump(
                    prepare_json_export(employee_db),
                    file,
                    ensure_ascii=False,
                    indent=4,
                )

            if status == 1:
                show_message("\n✅ Funcionário cadastrado com sucesso!", "green")
            elif status == 0:
                show_message("\n✅ Funcionário excluído com sucesso!", "green")
            else:
                show_message(f"\n✅ {len(employee_db)} funcionários exportados com sucesso!", "green")

            draw_divider("=")
            log_event(LOG_EXPORT, message=f"{len(employee_db)} funcionários exportados com sucesso.")
            pause()

        except FileNotFoundError:
            log_event(LOG_EXPORT, message="Arquivo ou diretório não encontrado.")

        except PermissionError:
            log_event(LOG_EXPORT, message="Permissão negada para escrever o arquivo.")

        except TypeError:
            log_event(LOG_EXPORT, message="Erro de serialização JSON.")

        except OSError:
            log_event(LOG_EXPORT, message="Erro de I/O ao gravar arquivo JSON.")

    def load_data(self):
        """
        Carrega os dados dos funcionários a partir de arquivos JSON ou CSV.

        Returns:
            None
        """
        log_event(LOG_LOAD, message="Iniciando verificação de arquivos de dados.")

        # Verifica se o arquivo JSON existe e contém dados
        if JSON_FILE.exists() and JSON_FILE.is_file() and JSON_FILE.stat().st_size > 0:
            show_message(f"\n📄 Arquivo '{JSON_FILE.name}' encontrado...", "green")
            draw_divider("-")
            log_event(LOG_LOAD, message=f"{JSON_FILE.name} encontrado. Solicitando importação")
            import_json(employee_db)

        else:
            show_message(f"\n📄 Arquivo '{JSON_FILE.name}' não encontrado.", "red")
            show_message(f"\n📄 Tentando importar o arquivo {CSV_FILE.name}.")

            log_event(LOG_LOAD, message="Arquivo JSON não encontrado. Tentando importar do CSV inicial")

            # Verifica se o arquivo CSV existe e contém dados
            if CSV_FILE.exists() and CSV_FILE.is_file() and CSV_FILE.stat().st_size > 0:
                log_event(LOG_LOAD, message=f"Arquivo {CSV_FILE.name} encontrado. Solicitando importação do CSV")
                import_csv(employee_db)

            else:
                show_message(f"\n⚠️ ATENÇÃO:\n('{JSON_FILE.name}' e '{CSV_FILE.name}') não encontrados!", "red")
                show_message("\n💻 O sistema iniciará sem dados carregados.")

                log_event(LOG_LOAD, message=f"JSON e CSV não encontrados. Criando arquivo vazio {JSON_FILE.name}")

                # Cria arquivo JSON vazio
                with open(JSON_FILE, "w", encoding="utf-8") as f:
                    json.dump({}, f)
                    log_event("create_file", message=f"Arquivo {JSON_FILE.name} vazio criado para iniciar o sistema.")

    def display_employee_search(self, employee, extra_fields):
        """
        Exibe os dados do funcionário em modo de consulta.

        Args:
            employee (Employee): Funcionário a ser exibido.
            extra_fields (list): Campos adicionais a serem exibidos.

        Returns:
            None
        """
        # Campos obrigatórios
        show_field("\nMatrícula:\t", employee.registration)
        show_field("Nome:\t\t", employee.full_name)
        show_field("CPF:\t\t", format_cpf(employee.cpf))

        # Campos extras
        if extra_fields:
            for field in extra_fields:
                if field == "birth_date":
                    show_field("D. Nasc:\t", date_to_str(employee.birth_date))
                elif field == "department":
                    show_field("Departamento:\t", employee.department)
                elif field == "role":
                    show_field("Cargo:\t\t", employee.role)
                elif field == "salary":
                    show_field("Salário:\t", format_brl_currency(employee.salary))
                elif field == "active":
                    status = "Ativo" if employee.active else "Inativo"
                    show_field("Status:\t\t", status)
