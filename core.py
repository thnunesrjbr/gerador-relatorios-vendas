import csv
import logging


def ler_vendas(caminho_arquivo: str) -> list[dict]:
    codificacoes = ['utf-8-sig', 'cp1252']

    logging.info(
        'Iniciando a leitura do arquivo %s.',
        caminho_arquivo,
    )

    for codificacao in codificacoes:
        try:
            vendas = []

            with open(
                caminho_arquivo,
                mode='r',
                encoding=codificacao,
                newline='',
            ) as arquivo:
                leitor = csv.DictReader(arquivo)

                for linha in leitor:
                    vendas.append({
                        'produto': linha['produto'].strip(),
                        'quantidade': int(linha['quantidade']),
                        'preco_unitario': float(
                            linha['preco_unitario']
                        ),
                    })

            logging.info(
                '%s vendas foram carregadas.',
                len(vendas),
            )

            return vendas

        except UnicodeDecodeError:
            logging.warning(
                'A codificação %s não funcionou.',
                codificacao,
            )

    raise ValueError(
        'Não foi possível identificar a codificação do arquivo.'
    )


def gerar_relatorio(vendas: list[dict]) -> dict:
    if not vendas:
        raise ValueError(
            'Nenhuma venda foi encontrada no arquivo.'
        )

    valor_total = 0.0
    totais_por_produto = {}
    quantidades_por_produto = {}

    for venda in vendas:
        produto = venda['produto']
        quantidade = venda['quantidade']
        preco_unitario = venda['preco_unitario']

        valor_venda = quantidade * preco_unitario

        valor_total += valor_venda

        totais_por_produto[produto] = (
            totais_por_produto.get(produto, 0.0)
            + valor_venda
        )

        quantidades_por_produto[produto] = (
            quantidades_por_produto.get(produto, 0)
            + quantidade
        )

    produto_mais_vendido = max(
        quantidades_por_produto,
        key=quantidades_por_produto.get,
    )

    logging.info('Relatório gerado com sucesso.')

    return {
        'valor_total': valor_total,
        'totais_por_produto': totais_por_produto,
        'produto_mais_vendido': produto_mais_vendido,
        'maior_quantidade': quantidades_por_produto[
            produto_mais_vendido
        ],
    }