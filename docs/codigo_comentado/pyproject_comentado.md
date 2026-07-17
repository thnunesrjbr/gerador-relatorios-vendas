# Explicação detalhada do `pyproject.toml`

Este documento explica, passo a passo, o arquivo:

```text
pyproject.toml
```

O arquivo original continua na pasta principal do projeto e é utilizado normalmente pelo Python, pelo `pip`, pelo `setuptools` e pelo `pytest`.

Esta documentação foi criada apenas para estudo.

---

# O que é o `pyproject.toml`

O `pyproject.toml` é um arquivo de configuração de projetos Python.

Ele pode guardar informações como:

- nome do projeto;
- versão;
- descrição;
- versão mínima do Python;
- dependências;
- ferramentas de desenvolvimento;
- forma de instalação;
- comandos de terminal;
- configurações do pytest;
- ferramenta usada para empacotar o projeto.

Neste projeto, ele também cria o comando:

```powershell
vendas-cli
```

Esse comando permite executar o programa sem precisar escrever:

```powershell
python cli.py
```

---

# Conteúdo completo do arquivo original

```toml
[build-system]
requires = ['setuptools>=68']
build-backend = 'setuptools.build_meta'


[project]
name = 'gerador-relatorios-vendas'
version = '0.1.0'
description = 'Programa de linha de comando para gerar relatórios de vendas a partir de arquivos CSV.'
requires-python = '>=3.9'
dependencies = []


[project.optional-dependencies]
dev = [
    'pytest>=9.0',
    'pytest-cov>=7.0',
]


[project.scripts]
vendas-cli = 'cli:main'


[tool.setuptools]
py-modules = [
    'core',
    'cli',
]


[tool.pytest.ini_options]
testpaths = [
    'tests',
]
addopts = '--basetemp=.pytest_temp'
```

---

# O que é TOML

TOML é um formato de configuração.

Ele tenta ser simples e legível.

Seu nome significa:

```text
Tom's Obvious, Minimal Language
```

Em um arquivo TOML, as configurações são organizadas em seções.

As seções aparecem entre colchetes.

Exemplo:

```toml
[project]
```

Dentro da seção, colocamos propriedades:

```toml
name = 'gerador-relatorios-vendas'
version = '0.1.0'
```

Podemos pensar assim:

```text
[seção]
propriedade = valor
```

---

# Seção `[build-system]`

```toml
[build-system]
requires = ['setuptools>=68']
build-backend = 'setuptools.build_meta'
```

Essa seção informa como o projeto deve ser preparado para instalação.

Podemos interpretar como:

> Python, use estas ferramentas para construir e instalar o projeto.

---

## Linha `[build-system]`

```toml
[build-system]
```

Cria a seção responsável pelo sistema de construção do projeto.

A palavra `build` significa construção.

Neste contexto, construir significa preparar o projeto para:

- instalação;
- empacotamento;
- criação de distribuição;
- criação de arquivos de instalação.

---

## Linha `requires`

```toml
requires = ['setuptools>=68']
```

Essa linha informa quais ferramentas são necessárias para construir o projeto.

A lista contém:

```text
setuptools
```

O `setuptools` é uma ferramenta muito usada no ecossistema Python.

Ele ajuda a:

- instalar projetos;
- localizar módulos;
- criar pacotes;
- criar comandos de terminal;
- preparar arquivos para distribuição.

A parte:

```text
>=68
```

significa:

> Use a versão 68 ou uma versão mais recente do setuptools.

Exemplos aceitos:

```text
68
69
70
75
80
```

Uma versão anterior à 68 não atende à exigência.

---

## Linha `build-backend`

```toml
build-backend = 'setuptools.build_meta'
```

Essa linha informa qual mecanismo será utilizado para construir o projeto.

O valor:

```text
setuptools.build_meta
```

aponta para o sistema de construção disponibilizado pelo `setuptools`.

Podemos pensar assim:

```text
Ferramenta escolhida: setuptools
Motor utilizado: setuptools.build_meta
```

---

# Seção `[project]`

```toml
[project]
name = 'gerador-relatorios-vendas'
version = '0.1.0'
description = 'Programa de linha de comando para gerar relatórios de vendas a partir de arquivos CSV.'
requires-python = '>=3.9'
dependencies = []
```

Essa seção guarda as informações principais do projeto.

É como a ficha de identificação do programa.

---

## Nome do projeto

```toml
name = 'gerador-relatorios-vendas'
```

Define o nome técnico do projeto.

Esse nome é utilizado durante a instalação.

Quando executamos:

```powershell
python -m pip install -e ".[dev]"
```

o terminal mostrou:

```text
Successfully installed gerador-relatorios-vendas-0.1.0
```

O nome exibido veio desta configuração.

Os hífens são comuns em nomes de projetos Python.

O nome do projeto não precisa ser igual ao nome de um arquivo Python.

Neste caso:

```text
Nome do projeto:
gerador-relatorios-vendas

Arquivos principais:
core.py
cli.py
```

---

## Versão do projeto

```toml
version = '0.1.0'
```

Define a versão atual.

O formato normalmente segue esta ideia:

```text
MAIOR.MENOR.CORREÇÃO
```

Neste exemplo:

```text
0.1.0
```

Podemos interpretar assim:

```text
0 → projeto ainda não chegou à versão principal 1
1 → primeira versão funcional
0 → nenhuma correção adicional dessa versão
```

Exemplos futuros:

```text
0.1.1
```

Pode representar uma pequena correção.

```text
0.2.0
```

Pode representar uma nova funcionalidade.

```text
1.0.0
```

Pode representar a primeira versão considerada estável e completa.

---

## Descrição

```toml
description = 'Programa de linha de comando para gerar relatórios de vendas a partir de arquivos CSV.'
```

Essa linha apresenta uma explicação curta sobre o projeto.

Ela informa:

- que o programa funciona por linha de comando;
- que gera relatórios;
- que utiliza arquivos CSV.

A descrição deve ser curta e objetiva.

O README possui uma explicação mais completa.

---

## Versão mínima do Python

```toml
requires-python = '>=3.9'
```

Essa configuração informa a versão mínima do Python necessária.

O símbolo:

```text
>=
```

significa:

```text
maior ou igual
```

Portanto:

```text
Python 3.9 ou superior
```

Exemplos aceitos:

```text
Python 3.9
Python 3.10
Python 3.11
Python 3.12
Python 3.13
```

Durante o desenvolvimento, foi utilizado:

```text
Python 3.13.7
```

Essa versão atende à exigência.

---

## Dependências principais

```toml
dependencies = []
```

Essa lista guarda bibliotecas necessárias para o programa funcionar.

Ela está vazia porque o programa utiliza apenas bibliotecas que já fazem parte do Python:

```text
csv
argparse
json
logging
```

Esses módulos fazem parte da biblioteca padrão.

Isso significa que uma pessoa não precisa instalar esses módulos separadamente.

Se o projeto utilizasse uma biblioteca externa, poderíamos escrever:

```toml
dependencies = [
    'requests>=2.0',
]
```

Mas isso não é necessário neste projeto.

---

# Seção `[project.optional-dependencies]`

```toml
[project.optional-dependencies]
dev = [
    'pytest>=9.0',
    'pytest-cov>=7.0',
]
```

Essa seção guarda dependências opcionais.

Elas não são necessárias para utilizar o programa.

Elas são necessárias para desenvolver, testar e analisar o projeto.

---

## Grupo `dev`

```toml
dev = [
    'pytest>=9.0',
    'pytest-cov>=7.0',
]
```

A palavra:

```text
dev
```

é uma abreviação de:

```text
development
```

Em português:

```text
desenvolvimento
```

Esse grupo possui duas bibliotecas:

```text
pytest
pytest-cov
```

---

## Dependência `pytest`

```toml
'pytest>=9.0'
```

O `pytest` executa os testes automatizados.

Ele procura arquivos e funções de teste.

Exemplos:

```text
tests/test_core.py
```

```python
def test_gerar_relatorio_com_uma_venda():
```

A parte:

```text
>=9.0
```

significa:

> Use pytest versão 9.0 ou superior.

---

## Dependência `pytest-cov`

```toml
'pytest-cov>=7.0'
```

O `pytest-cov` adiciona ao pytest a capacidade de medir cobertura.

A cobertura mostra quantas linhas do código foram executadas durante os testes.

O comando utilizado foi:

```powershell
python -m pytest --cov=core --cov-report=term-missing
```

O projeto alcançou:

```text
97% de cobertura no core.py
```

---

## Como instalar o grupo `dev`

O comando usado foi:

```powershell
python -m pip install -e ".[dev]"
```

A parte:

```text
[dev]
```

informa:

> Além do projeto, instale também as dependências do grupo dev.

Sem `[dev]`, o comando poderia ser:

```powershell
python -m pip install -e .
```

Nesse caso, pytest e pytest-cov não seriam instalados por meio desta configuração.

---

# Seção `[project.scripts]`

```toml
[project.scripts]
vendas-cli = 'cli:main'
```

Essa seção cria comandos de terminal.

Neste projeto, ela cria:

```text
vendas-cli
```

---

## Lado esquerdo

```toml
vendas-cli
```

É o nome do comando que o usuário executará.

Exemplo:

```powershell
vendas-cli vendas_exemplo.csv
```

---

## Lado direito

```toml
'cli:main'
```

Essa parte possui duas informações separadas por dois-pontos:

```text
cli
:
main
```

### `cli`

Representa o módulo:

```text
cli.py
```

Não escrevemos a extensão `.py`.

### `main`

Representa a função:

```python
def main() -> None:
```

Portanto:

```text
vendas-cli
    ↓
cli.py
    ↓
função main()
```

Quando o usuário executa:

```powershell
vendas-cli vendas_exemplo.csv
```

o Python inicia a função `main()` do arquivo `cli.py`.

---

# Seção `[tool.setuptools]`

```toml
[tool.setuptools]
py-modules = [
    'core',
    'cli',
]
```

Essa seção contém configurações específicas do `setuptools`.

Ela informa quais módulos Python fazem parte do projeto.

---

## Linha `py-modules`

```toml
py-modules = [
    'core',
    'cli',
]
```

Os módulos listados são:

```text
core.py
cli.py
```

Novamente, não escrevemos a extensão `.py`.

O `setuptools` entende:

```text
'core' → core.py
'cli' → cli.py
```

O arquivo `core.py` possui:

- leitura do CSV;
- geração do relatório;
- regras de negócio.

O arquivo `cli.py` possui:

- argumentos do terminal;
- exibição em texto;
- exibição em JSON;
- tratamento dos erros;
- função principal.

---

# Seção `[tool.pytest.ini_options]`

```toml
[tool.pytest.ini_options]
testpaths = [
    'tests',
]
addopts = '--basetemp=.pytest_temp'
```

Essa seção guarda configurações do pytest.

Assim, não precisamos repetir algumas opções toda vez no terminal.

---

## Linha `testpaths`

```toml
testpaths = [
    'tests',
]
```

Essa configuração informa onde o pytest deve procurar os testes.

Neste projeto, eles ficam na pasta:

```text
tests
```

Dentro dela existe:

```text
tests/test_core.py
```

Quando executamos:

```powershell
python -m pytest
```

o pytest lê esta configuração e procura os testes dentro da pasta indicada.

No terminal apareceu:

```text
configfile: pyproject.toml
testpaths: tests
```

Isso confirmou que a configuração foi reconhecida.

---

## Linha `addopts`

```toml
addopts = '--basetemp=.pytest_temp'
```

A palavra `addopts` significa adicionar opções.

Essa linha faz com que o pytest utilize automaticamente:

```text
--basetemp=.pytest_temp
```

Essa opção define a pasta temporária usada durante os testes.

Antes dessa configuração, o pytest utilizou a pasta temporária padrão do Windows e ocorreu:

```text
PermissionError: [WinError 5] Acesso negado
```

Os testes haviam passado, mas o pytest não conseguiu limpar a pasta temporária.

Para resolver, escolhemos uma pasta dentro do projeto:

```text
.pytest_temp
```

Agora, quando executamos:

```powershell
python -m pytest
```

é como se executássemos:

```powershell
python -m pytest --basetemp=.pytest_temp
```

A opção é aplicada automaticamente.

---

# Instalação editável

O comando utilizado foi:

```powershell
python -m pip install -e ".[dev]"
```

Vamos separar esse comando.

---

## `python -m pip`

```powershell
python -m pip
```

Executa o gerenciador de pacotes `pip` usando o Python atual.

Isso ajuda a garantir que o `pip` utilizado pertence à mesma instalação do Python.

---

## `install`

```text
install
```

Informa que queremos instalar algo.

---

## `-e`

```text
-e
```

Significa:

```text
editable
```

Em português:

```text
editável
```

Uma instalação editável continua apontando para os arquivos da pasta do projeto.

Assim, alterações feitas em:

```text
core.py
cli.py
```

ficam disponíveis sem precisar reinstalar o projeto a cada pequena mudança.

---

## O ponto

```text
.
```

O ponto representa a pasta atual.

Portanto:

```powershell
pip install .
```

significa:

> Instale o projeto encontrado na pasta atual.

O `pip` encontra o `pyproject.toml` nessa pasta e lê suas configurações.

---

## O grupo `[dev]`

```text
[dev]
```

Informa que também queremos instalar as dependências opcionais do grupo de desenvolvimento:

```text
pytest
pytest-cov
```

---

# Resultado da instalação

Depois do comando:

```powershell
python -m pip install -e ".[dev]"
```

o terminal mostrou:

```text
Successfully installed gerador-relatorios-vendas-0.1.0
```

Isso confirmou que:

- o `pyproject.toml` foi reconhecido;
- o projeto foi instalado;
- o nome e a versão estavam corretos;
- o comando `vendas-cli` foi criado;
- as dependências de desenvolvimento estavam disponíveis.

---

# Teste do comando instalado

Após a instalação, foi possível executar:

```powershell
vendas-cli vendas_exemplo.csv
```

Para saída JSON:

```powershell
vendas-cli vendas_exemplo.csv --format json
```

Para ajuda:

```powershell
vendas-cli --help
```

Isso confirmou que a seção:

```toml
[project.scripts]
vendas-cli = 'cli:main'
```

está funcionando corretamente.

---

# Resumo do arquivo

O `pyproject.toml` deste projeto realiza as seguintes tarefas:

```text
Define o sistema de construção
Define nome e versão
Define a versão mínima do Python
Registra dependências
Registra dependências de desenvolvimento
Cria o comando vendas-cli
Informa os módulos do projeto
Configura a pasta de testes
Configura a pasta temporária do pytest
```

Podemos visualizar o fluxo assim:

```text
pyproject.toml
    ↓
pip lê a configuração
    ↓
setuptools instala o projeto
    ↓
vendas-cli é criado
    ↓
pytest encontra a pasta tests
    ↓
o projeto pode ser instalado e testado
```

---

# Observação importante

Este arquivo:

```text
docs/codigo_comentado/pyproject_comentado.md
```

é somente uma documentação.

O arquivo de configuração verdadeiro continua sendo:

```text
pyproject.toml
```

Alterações feitas nesta documentação não modificam a instalação do projeto.