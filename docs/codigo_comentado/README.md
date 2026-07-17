# Documentação comentada do projeto

Esta pasta contém versões didáticas e detalhadamente comentadas dos principais arquivos do projeto:

```text
Gerador de Relatórios de Vendas
```

O objetivo desta documentação é ajudar iniciantes em Python a entender:

- como o projeto foi organizado;
- como os arquivos se comunicam;
- como o CSV é lido;
- como o relatório é calculado;
- como o programa recebe argumentos pelo terminal;
- como funcionam os testes automatizados;
- como o projeto é instalado;
- como o comando `vendas-cli` é criado.

---

# Aviso importante

Os arquivos desta pasta foram criados apenas para estudo.

O programa verdadeiro continua utilizando os arquivos localizados na pasta principal:

```text
core.py
cli.py
pyproject.toml
tests/test_core.py
```

As versões comentadas não substituem os arquivos originais.

Elas possuem muitos comentários porque foram preparadas para explicar cada etapa do projeto.

---

# Estrutura da documentação

```text
docs/
└── codigo_comentado/
    ├── README.md
    ├── core_comentado.py
    ├── cli_comentado.py
    ├── test_core_comentado.py
    └── pyproject_comentado.md
```

---

# Arquivos disponíveis

## `core_comentado.py`

Versão didática do arquivo:

```text
core.py
```

Esse arquivo explica:

- importação do módulo `csv`;
- importação do módulo `logging`;
- criação de funções;
- parâmetros e retorno;
- tipagem com `str`, `list` e `dict`;
- abertura de arquivos com `with open`;
- leitura de CSV com `csv.DictReader`;
- diferença entre UTF-8 e CP1252;
- funcionamento de `try` e `except`;
- tratamento de `UnicodeDecodeError`;
- uso de listas;
- uso de dicionários;
- conversão com `int` e `float`;
- uso de `.strip()`;
- uso de `.append()`;
- cálculo do valor das vendas;
- agrupamento de produtos;
- uso de `.get()`;
- soma de quantidades;
- uso de `max()`;
- retorno de um dicionário com o relatório.

Esse é o melhor arquivo para começar a estudar a lógica principal.

---

## `cli_comentado.py`

Versão didática do arquivo:

```text
cli.py
```

Esse arquivo explica:

- uso de `argparse`;
- criação de argumentos de terminal;
- argumento obrigatório;
- argumento opcional;
- uso de `choices`;
- uso de `default`;
- leitura de argumentos com `parse_args`;
- saída em texto;
- saída em JSON;
- uso de `json.dumps`;
- uso de `ensure_ascii`;
- uso de `indent`;
- formatação com f-string;
- alinhamento de textos;
- exibição de casas decimais;
- configuração de logs;
- tratamento de erros;
- funcionamento da função `main`;
- funcionamento de `if __name__ == '__main__'`.

Esse arquivo mostra como o usuário conversa com o programa pelo terminal.

---

## `test_core_comentado.py`

Versão didática do arquivo:

```text
tests/test_core.py
```

Esse arquivo explica:

- o que é um teste unitário;
- como o pytest encontra testes;
- por que funções de teste começam com `test_`;
- estrutura Arrange, Act e Assert;
- uso de `assert`;
- uso de `pytest.approx`;
- uso de `pytest.raises`;
- teste de erros esperados;
- funcionamento de `tmp_path`;
- criação de arquivos temporários;
- teste de arquivos UTF-8;
- teste de arquivos CP1252;
- teste de arquivo inexistente;
- verificação dos cálculos;
- cobertura de testes.

Esse arquivo ajuda a entender como validar automaticamente se o programa continua funcionando.

---

## `pyproject_comentado.md`

Documento didático sobre o arquivo:

```text
pyproject.toml
```

Esse documento explica:

- o que é TOML;
- funcionamento da seção `[build-system]`;
- uso do `setuptools`;
- nome do projeto;
- versão;
- descrição;
- versão mínima do Python;
- dependências;
- dependências de desenvolvimento;
- criação do grupo `dev`;
- funcionamento de `pytest`;
- funcionamento de `pytest-cov`;
- criação do comando `vendas-cli`;
- configuração dos módulos;
- configuração da pasta de testes;
- configuração da pasta temporária do pytest;
- instalação editável;
- funcionamento do comando `pip install -e ".[dev]"`.

Esse documento mostra como o projeto passou de arquivos Python comuns para um programa instalável.

---

# Ordem recomendada de estudo

A ordem recomendada é:

```text
1. core_comentado.py
2. cli_comentado.py
3. test_core_comentado.py
4. pyproject_comentado.md
```

## Etapa 1 — Entender a lógica

Comece por:

```text
core_comentado.py
```

Primeiro é importante entender:

- como o CSV é lido;
- como os dados são convertidos;
- como os cálculos são feitos;
- como o relatório é montado.

---

## Etapa 2 — Entender o terminal

Depois leia:

```text
cli_comentado.py
```

Nessa etapa, observe:

- como o caminho do arquivo é recebido;
- como o formato é escolhido;
- como o resultado é exibido;
- como erros são apresentados.

---

## Etapa 3 — Entender os testes

Depois leia:

```text
test_core_comentado.py
```

Nessa etapa, procure entender:

- como preparar os dados;
- como chamar uma função;
- como verificar o resultado;
- como testar erros;
- como usar arquivos temporários.

---

## Etapa 4 — Entender a instalação

Por último, leia:

```text
pyproject_comentado.md
```

Nessa etapa, observe:

- como o projeto é identificado;
- como as dependências são declaradas;
- como o comando `vendas-cli` é criado;
- como o pytest é configurado.

---

# Fluxo completo do projeto

O funcionamento geral pode ser representado assim:

```text
Usuário executa o comando
        ↓
vendas-cli vendas_exemplo.csv
        ↓
pyproject.toml aponta para cli.py
        ↓
cli.py executa main()
        ↓
argparse lê os argumentos
        ↓
cli.py chama ler_vendas()
        ↓
core.py abre o CSV
        ↓
core.py transforma as linhas em dicionários
        ↓
cli.py chama gerar_relatorio()
        ↓
core.py realiza os cálculos
        ↓
cli.py exibe texto ou JSON
```

---

# Fluxo dos testes

```text
python -m pytest
        ↓
pytest lê o pyproject.toml
        ↓
pytest procura a pasta tests
        ↓
pytest encontra test_core.py
        ↓
cada função test_ é executada
        ↓
os resultados são verificados com assert
        ↓
o pytest informa se os testes passaram
```

---

# Arquivos originais e arquivos comentados

## Arquivos originais

São utilizados pelo programa:

```text
core.py
cli.py
pyproject.toml
tests/test_core.py
```

## Arquivos comentados

São utilizados apenas para estudo:

```text
docs/codigo_comentado/core_comentado.py
docs/codigo_comentado/cli_comentado.py
docs/codigo_comentado/test_core_comentado.py
docs/codigo_comentado/pyproject_comentado.md
```

---

# Como executar o projeto original

Relatório em texto:

```powershell
vendas-cli vendas_exemplo.csv
```

Relatório em JSON:

```powershell
vendas-cli vendas_exemplo.csv --format json
```

Ajuda:

```powershell
vendas-cli --help
```

---

# Como executar os testes originais

```powershell
python -m pytest
```

Com cobertura:

```powershell
python -m pytest --cov=core --cov-report=term-missing
```

Resultado obtido durante o desenvolvimento:

```text
6 testes aprovados
97% de cobertura no core.py
```

---

# Objetivo educacional

Esta documentação procura apresentar o código de forma simples e progressiva.

Os comentários foram escritos para ajudar quem ainda está aprendendo conceitos como:

- variável;
- lista;
- dicionário;
- função;
- parâmetro;
- retorno;
- repetição;
- condição;
- tratamento de erro;
- módulo;
- importação;
- teste automatizado;
- linha de comando;
- instalação de projeto.

Os arquivos originais permanecem menores e mais limpos.

As versões comentadas servem como material complementar de estudo.