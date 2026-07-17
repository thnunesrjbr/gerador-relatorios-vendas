'''
Versão didática e comentada do arquivo cli.py.

Este arquivo foi criado apenas para documentação e estudo.

O programa principal continua utilizando o arquivo original:

    cli.py

Este arquivo explica, passo a passo:

- como o programa recebe comandos pelo terminal;
- como o argparse funciona;
- como o relatório é exibido em texto;
- como o relatório é convertido para JSON;
- como o logging é configurado;
- como os erros são tratados;
- como a função main organiza a execução;
- como funciona o if __name__ == '__main__'.

Este arquivo não precisa ser executado para o projeto funcionar.
'''


# Importa o módulo argparse.
#
# O argparse faz parte da biblioteca padrão do Python.
#
# Ele permite criar programas que recebem informações
# diretamente pelo terminal.
#
# Exemplo:
#
# vendas-cli vendas_exemplo.csv
#
# Nesse comando, o nome do arquivo CSV é recebido
# como argumento pelo programa.
import argparse


# Importa o módulo json.
#
# O json permite transformar objetos do Python,
# como listas e dicionários, em texto no formato JSON.
#
# Exemplo de dicionário Python:
#
# {
#     'valor_total': 599.3
# }
#
# Exemplo convertido para JSON:
#
# {
#     "valor_total": 599.3
# }
import json


# Importa o módulo logging.
#
# O logging permite mostrar mensagens sobre o que
# está acontecendo durante a execução.
#
# Exemplos:
#
# INFO:
# informa uma operação normal.
#
# WARNING:
# informa algo inesperado que não impediu a execução.
#
# ERROR:
# informa que ocorreu um problema.
import logging


# Importa duas funções do arquivo core.py.
#
# gerar_relatorio:
# recebe a lista de vendas e calcula o relatório.
#
# ler_vendas:
# recebe o caminho do CSV, abre o arquivo e devolve
# uma lista de vendas.
#
# A instrução:
#
# from core import ...
#
# significa:
#
# "Vá até o módulo core.py e importe estas funções."
from core import gerar_relatorio, ler_vendas


# Configura o comportamento geral do logging.
#
# basicConfig significa configuração básica.
#
# level=logging.INFO:
# define que mensagens de nível INFO ou superior
# serão exibidas.
#
# A ordem de importância é aproximadamente:
#
# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL
#
# Como escolhemos INFO, serão exibidas mensagens:
#
# INFO
# WARNING
# ERROR
# CRITICAL
#
# format='%(levelname)s: %(message)s':
# define o formato visual da mensagem.
#
# %(levelname)s:
# será substituído pelo nível da mensagem.
#
# %(message)s:
# será substituído pelo texto da mensagem.
#
# Exemplo:
#
# INFO: Relatório gerado com sucesso.
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s',
)


# Define a função exibir_relatorio.
#
# Essa função recebe:
#
# relatorio:
# um dicionário com os resultados calculados.
#
# formato:
# um texto indicando o formato de saída.
#
# Os formatos aceitos são:
#
# 'text'
# 'json'
#
# A indicação:
#
# relatorio: dict
#
# informa que o parâmetro deve receber um dicionário.
#
# formato: str
#
# informa que o parâmetro deve receber um texto.
#
# -> None
#
# informa que a função não devolve um valor.
#
# Ela apenas exibe informações no terminal.
def exibir_relatorio(
    relatorio: dict,
    formato: str,
) -> None:
    # Verifica se o formato escolhido foi JSON.
    #
    # O operador == faz uma comparação.
    #
    # Ele pergunta:
    #
    # "O conteúdo de formato é igual a 'json'?"
    if formato == 'json':
        # Exibe no terminal o relatório convertido para JSON.
        print(
            # json.dumps transforma um objeto Python em texto JSON.
            json.dumps(
                # Este é o dicionário que será convertido.
                relatorio,

                # ensure_ascii=False permite que caracteres como:
                #
                # ç
                # ã
                # é
                #
                # sejam exibidos normalmente.
                #
                # Sem essa opção, palavras poderiam aparecer assim:
                #
                # Cal\u00e7a
                ensure_ascii=False,

                # indent=4 cria uma identação de quatro espaços.
                #
                # Isso deixa o JSON mais fácil de ler.
                #
                # Sem indentação, o conteúdo apareceria
                # todo em uma única linha.
                indent=4,
            )
        )

        # O return encerra a função imediatamente.
        #
        # Isso evita que o programa continue e também
        # imprima o relatório em formato de texto.
        return

    # Se o formato não for JSON, o programa chega aqui
    # e começa a montar o relatório em texto.
    #
    # O operador * repete uma string.
    #
    # '=' * 60
    #
    # cria uma linha com sessenta sinais de igual.
    print('=' * 60)

    # Exibe o título do relatório.
    print('RELATÓRIO DE VENDAS')

    # Exibe outra linha com sessenta sinais de igual.
    print('=' * 60)

    # Exibe o cabeçalho da tabela.
    print(
        # Esta é uma f-string.
        #
        # Ela permite inserir valores e formatações
        # dentro de um texto.
        #
        # <30 significa:
        #
        # alinhar o conteúdo à esquerda
        # dentro de um espaço de trinta caracteres.
        f'{"Produto":<30}'

        # >20 significa:
        #
        # alinhar o conteúdo à direita
        # dentro de um espaço de vinte caracteres.
        f'{"Valor vendido":>20}'
    )

    # Cria uma linha de separação com sessenta hífens.
    print('-' * 60)

    # Percorre o dicionário de totais por produto.
    #
    # O conteúdo esperado é parecido com:
    #
    # {
    #     'Camiseta': 199.6,
    #     'Calça': 199.8,
    #     'Tênis': 199.9,
    # }
    #
    # O método items() devolve pares:
    #
    # chave e valor
    #
    # Neste caso:
    #
    # produto e valor
    for produto, valor in relatorio[
        'totais_por_produto'
    ].items():
        # Exibe uma linha da tabela para cada produto.
        print(
            # Alinha o nome do produto à esquerda
            # dentro de trinta caracteres.
            f'{produto:<30}'

            # Adiciona o texto R$.
            #
            # O valor é alinhado à direita.
            #
            # .2f significa:
            #
            # mostrar o número com duas casas decimais.
            #
            # Exemplo:
            #
            # 199.6 se torna 199.60
            f'R$ {valor:>10.2f}'
        )

    # Exibe uma linha de separação depois dos produtos.
    print('-' * 60)

    # Exibe o valor total de todas as vendas.
    print(
        # Alinha o texto Valor total à esquerda.
        f'{"Valor total:":<30}'

        # Busca o valor_total dentro do dicionário.
        #
        # Depois o formata com duas casas decimais.
        f'R$ {relatorio["valor_total"]:>10.2f}'
    )

    # Exibe o produto mais vendido.
    print(
        # Primeira parte da frase.
        'Produto mais vendido: '

        # Busca o nome do produto dentro do relatório.
        f'{relatorio["produto_mais_vendido"]} '

        # Busca a maior quantidade e exibe entre parênteses.
        f'({relatorio["maior_quantidade"]} unidades)'
    )

    # Exibe a última linha do relatório.
    print('=' * 60)


# Define a função principal do programa.
#
# O nome main é uma convenção muito comum.
#
# Ela funciona como ponto central da execução.
#
# Dentro dela, o programa:
#
# 1. configura os argumentos;
# 2. lê os argumentos do terminal;
# 3. abre o CSV;
# 4. gera o relatório;
# 5. exibe o resultado;
# 6. trata possíveis erros.
def main() -> None:
    # Cria o analisador de argumentos.
    #
    # ArgumentParser é uma classe do argparse.
    #
    # description define o texto exibido
    # quando alguém executa:
    #
    # vendas-cli --help
    parser = argparse.ArgumentParser(
        description='Gerador de relatório de vendas'
    )

    # Adiciona um argumento obrigatório chamado arquivo.
    #
    # Como ele não começa com hífen, o argumento
    # é considerado posicional e obrigatório.
    #
    # Exemplo:
    #
    # vendas-cli vendas_exemplo.csv
    #
    # Nesse caso:
    #
    # arquivo = 'vendas_exemplo.csv'
    parser.add_argument(
        'arquivo',

        # O help explica o argumento na tela de ajuda.
        help='Caminho do arquivo CSV de vendas',
    )

    # Adiciona um argumento opcional chamado --format.
    #
    # Argumentos que começam com -- são opcionais.
    #
    # Exemplo:
    #
    # vendas-cli vendas_exemplo.csv --format json
    parser.add_argument(
        '--format',

        # choices limita os valores aceitos.
        #
        # O usuário só poderá informar:
        #
        # text
        # json
        #
        # Qualquer outro valor gerará uma mensagem
        # automática de erro do argparse.
        choices=['text', 'json'],

        # default define o valor padrão.
        #
        # Se o usuário não informar --format,
        # o formato será text.
        default='text',

        # Texto exibido na ajuda.
        help='Formato de saída do relatório',
    )

    # Lê os argumentos que foram digitados no terminal.
    #
    # O resultado é guardado em argumentos.
    #
    # Exemplos:
    #
    # argumentos.arquivo
    # argumentos.format
    argumentos = parser.parse_args()

    # Inicia um bloco de tentativa.
    #
    # O código dentro do try pode gerar erros.
    #
    # Se isso acontecer, os blocos except tentarão
    # tratar o problema de forma amigável.
    try:
        # Chama a função ler_vendas.
        #
        # Envia o caminho recebido pelo terminal.
        #
        # O resultado será uma lista de vendas.
        vendas = ler_vendas(argumentos.arquivo)

        # Chama a função gerar_relatorio.
        #
        # Envia a lista de vendas.
        #
        # O resultado será um dicionário com os cálculos.
        relatorio = gerar_relatorio(vendas)

        # Chama a função responsável por mostrar
        # o relatório no terminal.
        exibir_relatorio(
            # Primeiro argumento:
            # dicionário com os resultados.
            relatorio,

            # Segundo argumento:
            # formato escolhido pelo usuário.
            argumentos.format,
        )

    # Captura especificamente o erro FileNotFoundError.
    #
    # Esse erro acontece quando o arquivo informado
    # não existe ou não pode ser localizado.
    except FileNotFoundError:
        # Registra uma mensagem de erro.
        #
        # %r mostra o valor usando sua representação.
        #
        # Normalmente o nome do arquivo aparecerá
        # entre aspas.
        #
        # Exemplo:
        #
        # ERROR: O arquivo 'vendas.csv' não foi encontrado.
        logging.error(
            'O arquivo %r não foi encontrado.',
            argumentos.arquivo,
        )

    # Captura três tipos de erro:
    #
    # KeyError:
    # geralmente acontece quando uma coluna esperada
    # não existe no CSV.
    #
    # TypeError:
    # acontece quando uma operação recebe um tipo
    # de dado incompatível.
    #
    # ValueError:
    # acontece quando um valor não pode ser convertido
    # ou processado corretamente.
    #
    # O trecho:
    #
    # as erro
    #
    # guarda o erro ocorrido dentro da variável erro.
    except (KeyError, TypeError, ValueError) as erro:
        # Exibe a mensagem do erro no terminal.
        logging.error('%s', erro)


# Esta condição verifica se o arquivo está sendo
# executado diretamente.
#
# Todo arquivo Python possui uma variável interna
# chamada __name__.
#
# Quando o arquivo é executado diretamente:
#
# python cli.py
#
# o valor de __name__ será:
#
# '__main__'
#
# Quando o arquivo é apenas importado por outro módulo,
# o valor de __name__ será o nome do módulo.
#
# Esta condição evita que main() seja executada
# automaticamente durante uma importação.
if __name__ == '__main__':
    # Chama a função principal e inicia o programa.
    main()