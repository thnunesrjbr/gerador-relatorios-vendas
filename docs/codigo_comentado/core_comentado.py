'''
Versão didática e comentada do arquivo core.py.

Este arquivo foi criado apenas para documentação e estudo.

O programa principal continua utilizando o arquivo original:

    core.py

Este arquivo comentado explica, passo a passo, como funciona:

- a leitura do arquivo CSV;
- a tentativa de diferentes codificações;
- a conversão dos dados;
- o cálculo das vendas;
- o agrupamento por produto;
- a identificação do produto mais vendido.

Ele não precisa ser executado para o programa funcionar.
'''


# Importa o módulo csv.
#
# O módulo csv faz parte da biblioteca padrão do Python.
#
# Ele possui ferramentas próprias para abrir e interpretar
# arquivos que possuem dados separados por vírgulas.
import csv


# Importa o módulo logging.
#
# O logging permite registrar mensagens sobre o que está
# acontecendo durante a execução do programa.
#
# Alguns exemplos de mensagens:
#
# INFO:
# informa que uma etapa foi executada normalmente.
#
# WARNING:
# informa que aconteceu algo inesperado, mas o programa
# ainda conseguiu continuar.
#
# ERROR:
# informa que ocorreu um problema que impediu uma operação.
import logging


# Define uma função chamada ler_vendas.
#
# Uma função é um bloco de código que executa uma tarefa específica.
#
# Neste caso, a tarefa é:
#
# 1. receber o caminho de um arquivo CSV;
# 2. abrir esse arquivo;
# 3. ler as vendas;
# 4. converter os dados;
# 5. devolver uma lista de vendas.
#
# O parâmetro caminho_arquivo recebeu a indicação de tipo str.
#
# str significa string, ou seja, um texto.
#
# Exemplo de valor recebido:
#
# 'vendas_exemplo.csv'
#
# A indicação:
#
# -> list[dict]
#
# informa que a função deve devolver uma lista de dicionários.
#
# Exemplo:
#
# [
#     {
#         'produto': 'Camiseta',
#         'quantidade': 2,
#         'preco_unitario': 50.0,
#     }
# ]
def ler_vendas(caminho_arquivo: str) -> list[dict]:
    # Cria uma lista contendo as codificações que serão testadas.
    #
    # A codificação determina como os caracteres de um arquivo
    # foram armazenados.
    #
    # O programa tentará primeiro:
    #
    # utf-8-sig
    #
    # Se não funcionar, tentará:
    #
    # cp1252
    #
    # CP1252 é uma codificação bastante comum em arquivos
    # criados no Windows.
    codificacoes = ['utf-8-sig', 'cp1252']

    # Registra uma mensagem informativa no terminal.
    #
    # O marcador %s será substituído pelo valor existente
    # na variável caminho_arquivo.
    #
    # Exemplo de resultado:
    #
    # INFO: Iniciando a leitura do arquivo vendas_exemplo.csv.
    logging.info(
        'Iniciando a leitura do arquivo %s.',
        caminho_arquivo,
    )

    # Inicia uma repetição.
    #
    # O for percorrerá cada item da lista codificacoes.
    #
    # Na primeira repetição:
    #
    # codificacao = 'utf-8-sig'
    #
    # Na segunda repetição:
    #
    # codificacao = 'cp1252'
    for codificacao in codificacoes:
        # Inicia um bloco try.
        #
        # O try significa:
        #
        # "Tente executar estas instruções."
        #
        # Se ocorrer um UnicodeDecodeError, o programa
        # seguirá para o bloco except correspondente.
        try:
            # Cria uma lista vazia.
            #
            # Essa lista será preenchida com as vendas
            # encontradas no arquivo CSV.
            vendas = []

            # Abre o arquivo informado pelo usuário.
            #
            # caminho_arquivo:
            # contém o endereço ou o nome do arquivo.
            #
            # mode='r':
            # informa que o arquivo será aberto para leitura.
            #
            # encoding=codificacao:
            # informa qual codificação será usada nesta tentativa.
            #
            # newline='':
            # evita problemas com quebras de linha durante
            # a leitura de arquivos CSV.
            #
            # O with garante que o arquivo será fechado
            # automaticamente depois da leitura.
            with open(
                caminho_arquivo,
                mode='r',
                encoding=codificacao,
                newline='',
            ) as arquivo:
                # Cria um leitor de CSV.
                #
                # O DictReader utiliza a primeira linha do CSV
                # como nome das colunas.
                #
                # Exemplo de cabeçalho:
                #
                # produto,quantidade,preco_unitario
                #
                # Cada linha será transformada em um dicionário.
                #
                # Exemplo:
                #
                # {
                #     'produto': 'Camiseta',
                #     'quantidade': '3',
                #     'preco_unitario': '49.9',
                # }
                leitor = csv.DictReader(arquivo)

                # Percorre cada linha encontrada pelo DictReader.
                #
                # A variável linha receberá um dicionário
                # por vez.
                for linha in leitor:
                    # Cria um novo dicionário com os dados
                    # da venda já organizados e convertidos.
                    #
                    # Em seguida, adiciona esse dicionário
                    # à lista vendas.
                    vendas.append({
                        # Obtém o valor da coluna produto.
                        #
                        # O método strip() remove espaços
                        # desnecessários no início e no final.
                        #
                        # Exemplo:
                        #
                        # ' Camiseta ' se torna 'Camiseta'.
                        'produto': linha['produto'].strip(),

                        # Obtém o valor da coluna quantidade.
                        #
                        # Os dados lidos de um CSV começam
                        # como texto.
                        #
                        # int() transforma o texto em número inteiro.
                        #
                        # Exemplo:
                        #
                        # '3' se torna 3.
                        'quantidade': int(linha['quantidade']),

                        # Obtém o valor da coluna preco_unitario.
                        #
                        # float() transforma o texto em um
                        # número que pode possuir casas decimais.
                        #
                        # Exemplo:
                        #
                        # '49.9' se torna 49.9.
                        'preco_unitario': float(
                            linha['preco_unitario']
                        ),
                    })

            # Registra quantas vendas foram carregadas.
            #
            # len(vendas) conta quantos itens existem
            # dentro da lista vendas.
            #
            # Exemplo:
            #
            # INFO: 4 vendas foram carregadas.
            logging.info(
                '%s vendas foram carregadas.',
                len(vendas),
            )

            # Devolve a lista de vendas para quem chamou
            # a função.
            #
            # Quando o return é executado, a função termina.
            return vendas

        # Este bloco será executado quando a codificação atual
        # não conseguir interpretar o conteúdo do arquivo.
        #
        # UnicodeDecodeError é um erro específico relacionado
        # à leitura de caracteres.
        except UnicodeDecodeError:
            # Registra um aviso informando que a codificação
            # atual não funcionou.
            #
            # Depois desse aviso, o for seguirá para a próxima
            # codificação da lista.
            logging.warning(
                'A codificação %s não funcionou.',
                codificacao,
            )

    # Esta linha só será alcançada se nenhuma das codificações
    # disponíveis conseguir ler o arquivo.
    #
    # raise serve para gerar um erro manualmente.
    #
    # ValueError indica que o programa recebeu ou encontrou
    # um valor que não pôde ser processado corretamente.
    raise ValueError(
        'Não foi possível identificar a codificação do arquivo.'
    )


# Define uma função chamada gerar_relatorio.
#
# Ela recebe uma lista de vendas.
#
# Cada venda deve ser um dicionário contendo:
#
# produto;
# quantidade;
# preco_unitario.
#
# A função devolverá um dicionário com:
#
# valor total;
# totais por produto;
# produto mais vendido;
# maior quantidade vendida.
def gerar_relatorio(vendas: list[dict]) -> dict:
    # Verifica se a lista vendas está vazia.
    #
    # Em Python, uma lista vazia é considerada falsa.
    #
    # Portanto:
    #
    # if not vendas
    #
    # significa:
    #
    # "Se não existem vendas..."
    if not vendas:
        # Gera um ValueError com uma mensagem clara.
        #
        # Isso impede que o programa tente gerar um relatório
        # sem possuir nenhuma venda.
        raise ValueError(
            'Nenhuma venda foi encontrada no arquivo.'
        )

    # Cria uma variável para acumular o valor de todas as vendas.
    #
    # Começa com 0.0 porque trabalharemos com valores decimais.
    valor_total = 0.0

    # Cria um dicionário vazio.
    #
    # Ele armazenará o valor total vendido de cada produto.
    #
    # Exemplo futuro:
    #
    # {
    #     'Camiseta': 199.6,
    #     'Calça': 199.8,
    # }
    totais_por_produto = {}

    # Cria outro dicionário vazio.
    #
    # Ele armazenará a quantidade total vendida de cada produto.
    #
    # Exemplo futuro:
    #
    # {
    #     'Camiseta': 4,
    #     'Calça': 2,
    # }
    quantidades_por_produto = {}

    # Percorre cada venda existente na lista vendas.
    #
    # Em cada repetição, a variável venda receberá
    # um dos dicionários da lista.
    for venda in vendas:
        # Obtém o nome do produto da venda atual.
        produto = venda['produto']

        # Obtém a quantidade vendida.
        quantidade = venda['quantidade']

        # Obtém o preço de uma unidade do produto.
        preco_unitario = venda['preco_unitario']

        # Calcula o valor daquela venda.
        #
        # Fórmula:
        #
        # quantidade multiplicada pelo preço unitário.
        #
        # Exemplo:
        #
        # 3 × 49.9 = 149.7
        valor_venda = quantidade * preco_unitario

        # Soma o valor da venda atual ao valor total.
        #
        # Esta forma:
        #
        # valor_total += valor_venda
        #
        # possui o mesmo efeito de:
        #
        # valor_total = valor_total + valor_venda
        valor_total += valor_venda

        # Atualiza o valor vendido daquele produto.
        #
        # totais_por_produto.get(produto, 0.0)
        #
        # procura o produto dentro do dicionário.
        #
        # Se o produto já existir, devolve o valor acumulado.
        #
        # Se o produto ainda não existir, devolve 0.0.
        #
        # Depois, soma o valor da venda atual.
        totais_por_produto[produto] = (
            totais_por_produto.get(produto, 0.0)
            + valor_venda
        )

        # Atualiza a quantidade total vendida daquele produto.
        #
        # quantidades_por_produto.get(produto, 0)
        #
        # procura a quantidade atual do produto.
        #
        # Se ainda não existir, começa em zero.
        #
        # Depois soma a quantidade da venda atual.
        quantidades_por_produto[produto] = (
            quantidades_por_produto.get(produto, 0)
            + quantidade
        )

    # Descobre qual produto possui a maior quantidade vendida.
    #
    # max() encontra o maior item de acordo com uma regra.
    #
    # O primeiro argumento é o dicionário:
    #
    # quantidades_por_produto
    #
    # Ao percorrer um dicionário, o Python percorre suas chaves,
    # ou seja, os nomes dos produtos.
    #
    # key=quantidades_por_produto.get
    #
    # informa que a comparação deve utilizar os valores
    # associados a cada produto.
    #
    # Exemplo:
    #
    # {
    #     'Camiseta': 4,
    #     'Calça': 2,
    # }
    #
    # O resultado será:
    #
    # 'Camiseta'
    produto_mais_vendido = max(
        quantidades_por_produto,
        key=quantidades_por_produto.get,
    )

    # Registra uma mensagem informando que o relatório
    # foi calculado com sucesso.
    logging.info('Relatório gerado com sucesso.')

    # Devolve um dicionário contendo o relatório completo.
    return {
        # Guarda a soma de todas as vendas.
        'valor_total': valor_total,

        # Guarda o dicionário com o valor vendido
        # de cada produto.
        'totais_por_produto': totais_por_produto,

        # Guarda o nome do produto com maior
        # quantidade vendida.
        'produto_mais_vendido': produto_mais_vendido,

        # Busca no dicionário de quantidades o valor
        # correspondente ao produto mais vendido.
        #
        # Exemplo:
        #
        # quantidades_por_produto['Camiseta']
        #
        # Resultado:
        #
        # 4
        'maior_quantidade': quantidades_por_produto[
            produto_mais_vendido
        ],
    }