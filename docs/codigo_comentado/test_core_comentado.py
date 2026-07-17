'''
Versão didática e comentada do arquivo tests/test_core.py.

Este arquivo foi criado apenas para documentação e estudo.

Os testes reais continuam no arquivo original:

    tests/test_core.py

Este arquivo explica:

- como o pytest encontra os testes;
- o que é um teste unitário;
- como funciona o assert;
- como testar valores numéricos;
- como testar erros esperados;
- como criar arquivos temporários;
- como testar arquivos UTF-8 e CP1252;
- como verificar arquivo inexistente.

Este arquivo não precisa ser executado para o projeto funcionar.
'''


# Importa a biblioteca pytest.
#
# O pytest é uma ferramenta utilizada para criar
# e executar testes automatizados em projetos Python.
#
# Ele oferece recursos como:
#
# pytest.approx()
# compara números decimais com tolerância.
#
# pytest.raises()
# verifica se um erro esperado foi gerado.
#
# tmp_path
# cria uma pasta temporária para o teste.
import pytest


# Importa as duas funções que serão testadas.
#
# gerar_relatorio:
# recebe uma lista de vendas e realiza os cálculos.
#
# ler_vendas:
# recebe o caminho de um CSV e transforma seu conteúdo
# em uma lista de dicionários.
from core import gerar_relatorio, ler_vendas


# Define o primeiro teste.
#
# O pytest procura automaticamente funções cujo nome
# começa com:
#
# test_
#
# Por isso, esta função será reconhecida como um teste.
#
# O nome também explica o cenário:
#
# gerar um relatório contendo apenas uma venda.
def test_gerar_relatorio_com_uma_venda():
    # Esta parte prepara os dados do teste.
    #
    # Em testes, essa etapa pode ser chamada de:
    #
    # Arrange
    #
    # Em português:
    #
    # Organizar ou preparar.
    #
    # Criamos uma lista contendo uma única venda.
    vendas = [
        {
            # Nome do produto.
            'produto': 'Camiseta',

            # Foram vendidas duas unidades.
            'quantidade': 2,

            # Cada unidade custa cinquenta reais.
            'preco_unitario': 50.0,
        }
    ]

    # Chama a função real do projeto.
    #
    # Esta etapa pode ser chamada de:
    #
    # Act
    #
    # Em português:
    #
    # Agir ou executar.
    #
    # A função deverá calcular:
    #
    # 2 × 50.0 = 100.0
    relatorio = gerar_relatorio(vendas)

    # Começa a etapa de verificação.
    #
    # Esta etapa pode ser chamada de:
    #
    # Assert
    #
    # Em português:
    #
    # Confirmar ou verificar.
    #
    # A palavra assert significa:
    #
    # "Confirme que esta condição é verdadeira."
    #
    # Verifica se o valor total calculado foi 100.0.
    assert relatorio['valor_total'] == 100.0

    # Verifica se o valor vendido por produto
    # foi armazenado corretamente.
    #
    # Como existe somente Camiseta, esperamos:
    #
    # {
    #     'Camiseta': 100.0
    # }
    assert relatorio['totais_por_produto'] == {
        'Camiseta': 100.0
    }

    # Verifica se Camiseta foi identificada
    # como produto mais vendido.
    assert relatorio['produto_mais_vendido'] == 'Camiseta'

    # Verifica se a maior quantidade encontrada foi dois.
    assert relatorio['maior_quantidade'] == 2


# Define o segundo teste.
#
# Este cenário verifica se o programa consegue somar
# registros repetidos do mesmo produto.
def test_gerar_relatorio_com_produtos_repetidos():
    # Prepara uma lista contendo três registros.
    vendas = [
        {
            # Primeira venda de Camiseta.
            #
            # 3 × 49.9 = 149.7
            'produto': 'Camiseta',
            'quantidade': 3,
            'preco_unitario': 49.9,
        },
        {
            # Segunda venda de Camiseta.
            #
            # 1 × 49.9 = 49.9
            'produto': 'Camiseta',
            'quantidade': 1,
            'preco_unitario': 49.9,
        },
        {
            # Venda de Calça.
            #
            # 2 × 99.9 = 199.8
            'produto': 'Calça',
            'quantidade': 2,
            'preco_unitario': 99.9,
        },
    ]

    # Executa a função gerar_relatorio.
    relatorio = gerar_relatorio(vendas)

    # O total esperado é:
    #
    # Camiseta:
    # 149.7 + 49.9 = 199.6
    #
    # Calça:
    # 199.8
    #
    # Total:
    # 199.6 + 199.8 = 399.4
    #
    # pytest.approx() é usado porque valores float
    # podem apresentar pequenas diferenças internas.
    #
    # Por exemplo, o computador poderia armazenar:
    #
    # 399.40000000000003
    #
    # mesmo que visualmente esperemos:
    #
    # 399.4
    assert relatorio['valor_total'] == pytest.approx(399.4)

    # Verifica os valores agrupados por produto.
    #
    # Também usamos pytest.approx porque os valores
    # são números decimais do tipo float.
    assert relatorio['totais_por_produto'] == pytest.approx({
        'Camiseta': 199.6,
        'Calça': 199.8,
    })

    # Camiseta vendeu:
    #
    # 3 + 1 = 4 unidades
    #
    # Calça vendeu:
    #
    # 2 unidades
    #
    # Portanto, Camiseta deve ser o produto mais vendido.
    assert relatorio['produto_mais_vendido'] == 'Camiseta'

    # Verifica se a maior quantidade acumulada foi quatro.
    assert relatorio['maior_quantidade'] == 4


# Define o terceiro teste.
#
# Este teste verifica o comportamento do programa
# quando nenhuma venda é informada.
def test_gerar_relatorio_com_lista_vazia():
    # pytest.raises() é usado quando esperamos que
    # determinada operação gere um erro.
    #
    # Neste caso, esperamos um ValueError.
    #
    # ValueError significa que um valor recebido
    # não pode ser utilizado naquela situação.
    #
    # O parâmetro match verifica se a mensagem do erro
    # contém o texto informado.
    with pytest.raises(
        ValueError,
        match='Nenhuma venda foi encontrada',
    ):
        # Envia uma lista vazia para gerar_relatorio.
        #
        # Como não existem vendas, a função deve gerar:
        #
        # ValueError
        gerar_relatorio([])


# Define o quarto teste.
#
# Este teste verifica se a função ler_vendas consegue
# abrir e interpretar um CSV em UTF-8.
#
# O parâmetro tmp_path é fornecido automaticamente
# pelo pytest.
def test_ler_vendas_com_arquivo_csv(tmp_path):
    # tmp_path é uma fixture do pytest.
    #
    # Uma fixture é um recurso que o pytest prepara
    # automaticamente para o teste.
    #
    # Neste caso, ele cria uma pasta temporária.
    #
    # O operador / junta a pasta temporária
    # com o nome do arquivo.
    arquivo_csv = tmp_path / 'vendas.csv'

    # write_text() cria o arquivo e grava o texto.
    #
    # O conteúdo criado será:
    #
    # produto,quantidade,preco_unitario
    # Camiseta,2,50.0
    # Calça,1,100.0
    #
    # O símbolo \n representa uma quebra de linha.
    #
    # encoding='utf-8-sig' define a codificação
    # utilizada para salvar o arquivo temporário.
    arquivo_csv.write_text(
        'produto,quantidade,preco_unitario\n'
        'Camiseta,2,50.0\n'
        'Calça,1,100.0\n',
        encoding='utf-8-sig',
    )

    # Chama a função ler_vendas.
    #
    # arquivo_csv é um objeto de caminho.
    #
    # str() transforma esse caminho em texto.
    vendas = ler_vendas(str(arquivo_csv))

    # Verifica se a função devolveu exatamente
    # a estrutura esperada.
    #
    # Também confirma se:
    #
    # quantidade foi convertida para int;
    # preco_unitario foi convertido para float;
    # os produtos foram lidos corretamente.
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


# Define o quinto teste.
#
# Este teste verifica a segunda codificação
# suportada pelo programa:
#
# CP1252
def test_ler_vendas_com_cp1252(tmp_path):
    # Cria o caminho do arquivo temporário.
    arquivo_csv = tmp_path / 'vendas_cp1252.csv'

    # Cria o CSV utilizando a codificação CP1252.
    #
    # A palavra Calça possui o caractere ç.
    #
    # Esse caractere ajuda a fazer a primeira tentativa
    # com UTF-8 falhar.
    #
    # Depois disso, o programa deve tentar CP1252
    # e conseguir ler o arquivo.
    arquivo_csv.write_text(
        'produto,quantidade,preco_unitario\n'
        'Calça,1,99.9\n',
        encoding='cp1252',
    )

    # Executa a leitura do arquivo temporário.
    vendas = ler_vendas(str(arquivo_csv))

    # Verifica se o produto com ç foi lido corretamente.
    #
    # Também verifica a conversão de quantidade e preço.
    assert vendas == [
        {
            'produto': 'Calça',
            'quantidade': 1,
            'preco_unitario': 99.9,
        }
    ]


# Define o sexto teste.
#
# Este teste verifica o comportamento do programa
# quando o usuário informa um arquivo inexistente.
def test_ler_vendas_com_arquivo_inexistente():
    # Esperamos que a função gere FileNotFoundError.
    #
    # FileNotFoundError significa:
    #
    # "O arquivo informado não foi encontrado."
    with pytest.raises(FileNotFoundError):
        # Informa propositalmente um nome de arquivo
        # que não existe.
        ler_vendas('arquivo_que_nao_existe.csv')