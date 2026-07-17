# Gerador de Relatórios de Vendas

Aplicação de linha de comando desenvolvida em Python para ler arquivos CSV de vendas e gerar relatórios consolidados.

O projeto permite calcular o valor total das vendas, o valor vendido por produto e identificar o produto com maior quantidade vendida.

## Funcionalidades

- Leitura de arquivos CSV.
- Suporte às codificações UTF-8 e CP1252.
- Cálculo do valor total das vendas.
- Cálculo do valor vendido por produto.
- Identificação do produto mais vendido por quantidade.
- Exibição do relatório em formato de texto.
- Exibição do relatório em formato JSON.
- Tratamento de erros.
- Registro de logs.
- Execução por linha de comando.
- Testes automatizados com pytest.
- Medição de cobertura com pytest-cov.
- Documentação comentada para estudo.

## Tecnologias utilizadas

- Python 3.
- csv.
- argparse.
- json.
- logging.
- pytest.
- pytest-cov.
- setuptools.

As bibliotecas `csv`, `argparse`, `json` e `logging` fazem parte da biblioteca padrão do Python.

## Estrutura do projeto

```text
gerador-relatorios-vendas/
├── .gitignore
├── README.md
├── cli.py
├── core.py
├── pyproject.toml
├── vendas_exemplo.csv
├── tests/
│   └── test_core.py
└── docs/
    └── codigo_comentado/
        ├── README.md
        ├── cli_comentado.py
        ├── core_comentado.py
        ├── pyproject_comentado.md
        └── test_core_comentado.py
```

## Descrição dos arquivos principais

- `core.py`: contém a leitura do CSV e as regras de negócio do relatório.
- `cli.py`: contém os argumentos do terminal e a exibição dos resultados.
- `pyproject.toml`: contém as configurações de instalação, testes e criação do comando `vendas-cli`.
- `vendas_exemplo.csv`: arquivo utilizado para demonstrar o funcionamento do projeto.
- `tests/test_core.py`: contém os testes automatizados do módulo `core.py`.
- `README.md`: contém a documentação principal do projeto.
- `.gitignore`: informa ao Git quais arquivos temporários não devem ser enviados ao repositório.

## Documentação comentada

A pasta:

```text
docs/codigo_comentado
```

contém versões didáticas e detalhadamente comentadas dos principais arquivos do projeto.

Essa documentação foi criada para ajudar iniciantes a entender como cada parte funciona.

Os arquivos disponíveis são:

- `core_comentado.py`: explicação detalhada da leitura do CSV e da geração do relatório.
- `cli_comentado.py`: explicação detalhada da linha de comando, da saída em texto e JSON e do tratamento de erros.
- `test_core_comentado.py`: explicação detalhada dos testes automatizados.
- `pyproject_comentado.md`: explicação detalhada da instalação e configuração do projeto.
- `README.md`: índice da documentação e ordem recomendada de estudo.

Os arquivos comentados são apenas material de estudo.

O programa verdadeiro continua utilizando:

```text
core.py
cli.py
pyproject.toml
tests/test_core.py
```

## Ordem recomendada de estudo

Para entender o projeto de forma progressiva, a ordem sugerida é:

```text
1. docs/codigo_comentado/core_comentado.py
2. docs/codigo_comentado/cli_comentado.py
3. docs/codigo_comentado/test_core_comentado.py
4. docs/codigo_comentado/pyproject_comentado.md
```

## Formato esperado do CSV

O arquivo CSV deve conter as seguintes colunas:

```csv
produto,quantidade,preco_unitario
Camiseta,3,49.9
Calça,2,99.9
Camiseta,1,49.9
Tênis,1,199.9
```

### Significado das colunas

- `produto`: nome do produto vendido.
- `quantidade`: quantidade vendida.
- `preco_unitario`: preço de uma unidade do produto.

## Instalação

Abra o PowerShell na pasta principal do projeto e execute:

```powershell
python -m pip install -e ".[dev]"
```

Esse comando instala o projeto em modo editável e também instala as dependências de desenvolvimento.

Após a instalação, o comando `vendas-cli` ficará disponível no terminal.

## Como executar

### Gerar relatório em texto

```powershell
vendas-cli vendas_exemplo.csv
```

Exemplo de saída:

```text
INFO: Iniciando a leitura do arquivo vendas_exemplo.csv.
WARNING: A codificação utf-8-sig não funcionou.
INFO: 4 vendas foram carregadas.
INFO: Relatório gerado com sucesso.
============================================================
RELATÓRIO DE VENDAS
============================================================
Produto                              Valor vendido
------------------------------------------------------------
Camiseta                      R$     199.60
Calça                         R$     199.80
Tênis                         R$     199.90
------------------------------------------------------------
Valor total:                  R$     599.30
Produto mais vendido: Camiseta (4 unidades)
============================================================
```

### Gerar relatório em JSON

```powershell
vendas-cli vendas_exemplo.csv --format json
```

Exemplo de saída:

```json
{
    "valor_total": 599.3,
    "totais_por_produto": {
        "Camiseta": 199.6,
        "Calça": 199.8,
        "Tênis": 199.9
    },
    "produto_mais_vendido": "Camiseta",
    "maior_quantidade": 4
}
```

### Consultar a ajuda do programa

```powershell
vendas-cli --help
```

## Argumentos disponíveis

### Arquivo CSV

O caminho do arquivo é um argumento obrigatório.

```powershell
vendas-cli vendas_exemplo.csv
```

Também é possível informar um caminho completo:

```powershell
vendas-cli "C:\Users\Usuario\Documentos\vendas.csv"
```

### Formato de saída

O argumento `--format` aceita dois valores:

- `text`: relatório formatado para leitura no terminal.
- `json`: relatório estruturado em JSON.

O formato padrão é `text`.

```powershell
vendas-cli vendas_exemplo.csv --format text
```

```powershell
vendas-cli vendas_exemplo.csv --format json
```

## Funcionamento geral

O fluxo principal do programa é:

```text
Usuário executa vendas-cli
        ↓
cli.py recebe os argumentos
        ↓
ler_vendas() abre o CSV
        ↓
as linhas são convertidas em dicionários
        ↓
gerar_relatorio() realiza os cálculos
        ↓
cli.py exibe o resultado em texto ou JSON
```

## Testes automatizados

Para executar os testes:

```powershell
python -m pytest
```

Os testes verificam:

- geração de relatório com uma venda;
- agrupamento de produtos repetidos;
- cálculo do valor total;
- identificação do produto mais vendido;
- tratamento de lista vazia;
- leitura de arquivo em UTF-8;
- leitura de arquivo em CP1252;
- tratamento de arquivo inexistente.

## Cobertura dos testes

Para executar os testes e medir a cobertura:

```powershell
python -m pytest --cov=core --cov-report=term-missing
```

Resultado obtido durante o desenvolvimento:

```text
Name      Stmts   Miss  Cover   Missing
---------------------------------------
core.py      34      1    97%   47
---------------------------------------
TOTAL        34      1    97%
```

A cobertura obtida no módulo `core.py` foi de 97%.

## Tratamento de erros

O programa possui tratamento para situações como:

- arquivo não encontrado;
- arquivo sem vendas;
- dados incompatíveis com os tipos esperados;
- colunas ausentes;
- problemas na codificação do arquivo.

Os erros são apresentados no terminal por meio do módulo `logging`.

## Codificação dos arquivos

O programa tenta ler o arquivo utilizando as seguintes codificações:

1. UTF-8 com suporte a BOM.
2. CP1252.

Essa estratégia permite trabalhar com arquivos CSV gerados por diferentes programas no Windows.

## Instalação editável

O projeto é instalado utilizando:

```powershell
python -m pip install -e ".[dev]"
```

A opção `-e` significa instalação editável.

Isso permite alterar os arquivos do projeto sem precisar reinstalar o programa após cada modificação.

O grupo `[dev]` instala também:

- pytest;
- pytest-cov.

## Comando `vendas-cli`

O comando é criado pelo arquivo `pyproject.toml`:

```toml
[project.scripts]
vendas-cli = 'cli:main'
```

Essa configuração significa:

```text
vendas-cli
    ↓
arquivo cli.py
    ↓
função main()
```

## Limitações atuais

- O projeto não possui filtro de vendas por intervalo de datas.
- O CSV utilizado atualmente não possui uma coluna de data.
- Os valores monetários são calculados utilizando o tipo `float`.
- A validação das colunas do CSV ainda é básica.

## Melhorias futuras

- Implementar filtro por data inicial e data final.
- Adicionar uma coluna de data ao CSV.
- Utilizar `Decimal` para cálculos monetários.
- Criar validações mais detalhadas para as colunas.
- Adicionar testes para o módulo `cli.py`.
- Permitir salvar o relatório diretamente em um arquivo.
- Melhorar a formatação dos valores monetários para o padrão brasileiro.
- Criar integração contínua com GitHub Actions.
- Publicar uma versão instalável do projeto.

## Autor

Thiago Nunes Costa dos Santos