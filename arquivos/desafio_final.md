# Projeto: Sistema Básico de Gestão de Funcionários

## Objetivo

Neste projeto, desenvolveremos um sistema em Python para o cadastro e a gestão básica de funcionários de uma empresa. O foco inicial é a implementação das funcionalidades essenciais de um sistema CRUD (Create, Read, Update, Delete) de forma simples, utilizando estruturas de dados nativas do Python e conceitos de lógica de programação. Deve ser usado somente o conteúdo visto em aula e bibliotecas pontuais do python, sem uso de orientação a objetos, classes e/ou modularização do programa.

&nbsp;

## Conceitos que serão aplicados

- Coerção de tipos (ex: transformar string em número)
- Dicionários e listas
- Funções e composição de funções
- Operadores lógicos (and, or, not)
- Operadores de coalescência (or / get)
- Operador ternário
- Condicionais if/else e simulação de switch
- Laços while, for
- try/except/finally para erros
- Estruturação de menu de opções
- Geração e uso de logs
- Métodos funcionais
- Tuplas nomeadas

&nbsp;

## Sobre sistema

O sistema permitirá as seguintes operações:

1.  **Inserir Funcionários:**
    * Cadastrar novos funcionários manualmente no sistema.
    * Cada funcionário deverá possuir os seguintes atributos:
        * `matricula: int` (única - não se repete)
        * `nome completo: str`
        * `cpf: str`
        * `data de nascimento: datetime` (informar no formato `dd/mm/yyyy`), armazenar como datetime.
        * `departamento: str`
        * `cargo: str`
        * `ativo: bool` (`True` para ativo, `False` para inativo)
        * `salario: float`

2.  **Consultar Funcionários:**
    * Permitir a consulta de funcionários.
    * A pesquisa pode ser realizada pelo `nome_completo`, `cpf` ou `matricula` do funcionário, aceitando **correspondência parcial** (ou seja, encontrar um funcionário mesmo que apenas parte dos dados sejam digitados).
    * Se quiserem, podem fazer um menu extra pedindo qual dos dados vai ser usado para consulta.
    * Ao exibir os dados do funcionário, deve ser exibido obrigatoriamente a matrícula, nome completo e cpf do funcionário.
    * Deve ser solicitado também, ao usuário, informar quais campos extras devem aparecer, funcionando como um filtro de dados. 
    * O usuário pode optar por não exibir nenhum campo extra, mas se quiser exibir algum a mais, deve ser possível.
    * Esse filtro deve ser dinâmico, permitindo que o usuário escolha quais campos (dentre os existentes) serão usados como filtro, e qual valor será filtrado.
        * Por exemplo: Além dos 3 obrigatórios, o usuário quer ver o departamento, mas somente os funcionários cujo departamento seja de Marketing. 
    * Todos os dados devem ser apresentados de forma legível ao usuário (data formatada, moeda formatada, etc.)
    * O formato de exibição dos dados é de livre escolha (somente os campos - nome e valor - na tela, tabela, json, etc.)

3.  **Listar Funcionários:**
    * Exibir todos os funcionários cadastrados no sistema.
    * Deve ser permitido escolher se apresenta somente os funcionários ativos, somente os inativos ou todos os funcionários. Deve aparecer também uma opção para voltar ao menu principal.
    * Caso selecionada a opção de todos os funcionários, a lista deverá exibir primeiro todos os funcionários que estão `ativos`, seguidos pelos funcionários `inativos`.
    * Dentro da listagem de ativos/inativos, exibir em ordem alfabética pelo nome do usuário.
    * Todos os dados devem ser apresentados de forma legível ao usuário (data formatada, moeda formatada, etc.)
    * O formato de exibição dos dados é de livre escolha (somente os campos - nome e valor - na tela, tabela, json, etc.)

4.  **Apagar Funcionários:**
    * Realizar a "exclusão" de um funcionário do sistema.
    * A exclusão não será física, mas lógica, alterando o status do funcionário para `ativo = False`.

5.  **Calcular folha de pagamento**
    * Exibir na tela a soma do salário de todos os funcionários ativos, formatando para a moeda corrente.

5.  **Exportar funcionários:**
    * Criar um arquivo chamado "funcionarios.json" contendo todos os dados dos funcionários no formato json, e salvar no diretório que o programa está rodando.
    * Caso o arquivo já exista, sobreescrever o antigo.
    * A criação do arquivo deve ser feita somente se o usuário selecionar a exportação dos funcionários.

### Estrutura de dados / banco de dados

Para o armazenamento dos dados dos funcionários no programa, utilize um **dicionário**. Utilize uma tupla nomeada (named tuple) para armazenar os atributos do funcionário.

### Funcionamento do sistema

* Ao abrir o programa pela primeira vez, importar o arquivo `funcionarios.csv` (já fornecido) e incluir esses funcionários no programa.
* Ao abrir o programa novamente, caso exista o arquivo `funcionarios.json`, importar ele. Caso não exista, importar o `funcionarios.csv`
* O programa não deve parar. Ou seja, caso ocorram falhas ou exceções, devem ser exibidas mensagens no console e o programa deve continuar em execução. Por exemplo: 
    * Se o menu apresenta opções de "1" a "5", e o usuário digitar "6", deve ser exibida uma mensagem e apresentar o menu novamente. 
    * Se o telefone deve ser digitado somente com números, e o usuário colocar "(" ou "-", informar que deve ser somente dígitos e pedir novamente o telefone.
* Cada ação realizada no programa deve gravar um log no arquivo `logs.txt`. Mais detalhes, consultar a seção "logs" abaixo.
*  

### Logs

* ok    -   Os logs devem ser salvos no arquivo "logs.txt".
* +-ok  -   Os logs podem ser salvos durante a ação ou salvos todos ao encerrar o programa.
* ok    -   Cada execução do programa deve gerar um novo arquivo. Caso o arquivo já exista, sobrescreva ele.
* Os logs devem conter as seguintes informações:
    ok  -   * datetime (dia, mes ano, hora, minuto e segundo)
    * ação (adicionar funcionário, Remover funcionário, listar, etc.) Todas as ações do menu devem estar inclusas nos logs.
    * Ao adicionar funcionários, informar todos os dados do funcionário adicionado. 
    * Ao remover, informar a matrícula do funcionário removido
    * Ao consultar, informar a matrícula do funcionário consultado
    * Os demais, só informar a ação, sem mais dados. Ex: Listagem, exportação, importação de funcionários, etc.
    * O formato dos logs deve ser:
        * Adicionar: `datetime - ação - dados do usuário (json serializado para string) - mensagem`. Por exemplo:
            * 2025-09-17T08:00:00 - adicionar - {matricula: 1, nome: bruno} - adicionado com sucesso
        * Remover: `datetime - ação - matricula - mensagem`
        * Demais: `datetime - ação - mensagem`

&nbsp;

## Regras para entrega

### Informações gerais

* Os grupos devem conter entre 4 e 5 participantes (livre escolha dos integrantes do grupo)
* A entrega deve ser feita no **LMS**, e pode ser através do link do github ou um arquivo .zip com o arquivo principal (o main.py). 
    * Não é necessário criar novos arquivos/módulos. Deve ficar tudo no mesmo arquivo. 
* Todos os integrantes do grupo devem enviar o trabalho, e todos devem enviar o mesmo arquivo.
* Deve ser indicado, através de comentários, quem fez a implementação da função. Por exemplo:

```python
def adicionar_funcionario():
    # Bruno Bragança
    pass
```


### Data de entrega
* 01/10/2025, às 23:59

### Apresentação
* No dia 01/10/2025 deve ser feita uma apresentação curta, demonstrando as principais funcionalidades do sistema. Não é necessário explicar função a função do código.
* Essa apresentação deve ter no máximo 10 minutos, pois serão muitos grupos.
