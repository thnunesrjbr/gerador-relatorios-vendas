import argparse
import json
import logging

from core import gerar_relatorio, ler_vendas


logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s',
)


def exibir_relatorio(
    relatorio: dict,
    formato: str,
) -> None:
    if formato == 'json':
        print(
            json.dumps(
                relatorio,
                ensure_ascii=False,
                indent=4,
            )
        )

        return

    print('=' * 60)
    print('RELATÓRIO DE VENDAS')
    print('=' * 60)
    print(
        f'{"Produto":<30}'
        f'{"Valor vendido":>20}'
    )
    print('-' * 60)

    for produto, valor in relatorio[
        'totais_por_produto'
    ].items():
        print(
            f'{produto:<30}'
            f'R$ {valor:>10.2f}'
        )

    print('-' * 60)
    print(
        f'{"Valor total:":<30}'
        f'R$ {relatorio["valor_total"]:>10.2f}'
    )
    print(
        'Produto mais vendido: '
        f'{relatorio["produto_mais_vendido"]} '
        f'({relatorio["maior_quantidade"]} unidades)'
    )
    print('=' * 60)


def main() -> None:
    parser = argparse.ArgumentParser(
        description='Gerador de relatório de vendas'
    )

    parser.add_argument(
        'arquivo',
        help='Caminho do arquivo CSV de vendas',
    )

    parser.add_argument(
        '--format',
        choices=['text', 'json'],
        default='text',
        help='Formato de saída do relatório',
    )

    argumentos = parser.parse_args()

    try:
        vendas = ler_vendas(argumentos.arquivo)
        relatorio = gerar_relatorio(vendas)

        exibir_relatorio(
            relatorio,
            argumentos.format,
        )

    except FileNotFoundError:
        logging.error(
            'O arquivo %r não foi encontrado.',
            argumentos.arquivo,
        )

    except (KeyError, TypeError, ValueError) as erro:
        logging.error('%s', erro)


if __name__ == '__main__':
    main()