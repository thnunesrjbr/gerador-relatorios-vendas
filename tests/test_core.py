import pytest

from core import gerar_relatorio, ler_vendas


def test_gerar_relatorio_com_uma_venda():
    vendas = [
        {
            'produto': 'Camiseta',
            'quantidade': 2,
            'preco_unitario': 50.0,
        }
    ]

    relatorio = gerar_relatorio(vendas)

    assert relatorio['valor_total'] == 100.0
    assert relatorio['totais_por_produto'] == {
        'Camiseta': 100.0
    }
    assert relatorio['produto_mais_vendido'] == 'Camiseta'
    assert relatorio['maior_quantidade'] == 2


def test_gerar_relatorio_com_produtos_repetidos():
    vendas = [
        {
            'produto': 'Camiseta',
            'quantidade': 3,
            'preco_unitario': 49.9,
        },
        {
            'produto': 'Camiseta',
            'quantidade': 1,
            'preco_unitario': 49.9,
        },
        {
            'produto': 'Calça',
            'quantidade': 2,
            'preco_unitario': 99.9,
        },
    ]

    relatorio = gerar_relatorio(vendas)

    assert relatorio['valor_total'] == pytest.approx(399.4)

    assert relatorio['totais_por_produto'] == pytest.approx({
        'Camiseta': 199.6,
        'Calça': 199.8,
    })

    assert relatorio['produto_mais_vendido'] == 'Camiseta'
    assert relatorio['maior_quantidade'] == 4


def test_gerar_relatorio_com_lista_vazia():
    with pytest.raises(
        ValueError,
        match='Nenhuma venda foi encontrada',
    ):
        gerar_relatorio([])


def test_ler_vendas_com_arquivo_csv(tmp_path):
    arquivo_csv = tmp_path / 'vendas.csv'

    arquivo_csv.write_text(
        'produto,quantidade,preco_unitario\n'
        'Camiseta,2,50.0\n'
        'Calça,1,100.0\n',
        encoding='utf-8-sig',
    )

    vendas = ler_vendas(str(arquivo_csv))

    assert vendas == [
        {
            'produto': 'Camiseta',
            'quantidade': 2,
            'preco_unitario': 50.0,
        },
        {
            'produto': 'Calça',
            'quantidade': 1,
            'preco_unitario': 100.0,
        },
    ]


def test_ler_vendas_com_cp1252(tmp_path):
    arquivo_csv = tmp_path / 'vendas_cp1252.csv'

    arquivo_csv.write_text(
        'produto,quantidade,preco_unitario\n'
        'Calça,1,99.9\n',
        encoding='cp1252',
    )

    vendas = ler_vendas(str(arquivo_csv))

    assert vendas == [
        {
            'produto': 'Calça',
            'quantidade': 1,
            'preco_unitario': 99.9,
        }
    ]


def test_ler_vendas_com_arquivo_inexistente():
    with pytest.raises(FileNotFoundError):
        ler_vendas('arquivo_que_nao_existe.csv')