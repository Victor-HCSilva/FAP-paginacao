import csv
import random

def gerar_dados_falsos(num_registros=30):
    """
    Gera dados falsos para um arquivo CSV com 30 registros.

    Args:
        num_registros: Número de registros a serem gerados (padrão: 30).

    Returns:
        Um dicionário contendo uma lista de dados para cada coluna.
    """

    nomes_produtos = ["Camiseta", "Calça", "Sapato", "Livro", "Celular", "Notebook", "Mesa", "Cadeira", "Caneca", "Relógio"]
    precos = [random.randint(10, 100) for _ in range(num_registros)]
    quantidades = [random.randint(1, 50) for _ in range(num_registros)]

    dados = {
        "nome_produto": [random.choice(nomes_produtos) for _ in range(num_registros)],
        "preco": precos,
        "quantidade": quantidades
    }

    return dados

def criar_arquivo_csv(dados, nome_arquivo="produtos.csv"):
    """
    Cria um arquivo CSV com os dados fornecidos.

    Args:
        dados: Um dicionário contendo listas de dados para cada coluna.
        nome_arquivo: Nome do arquivo CSV a ser criado (padrão: "produtos.csv").
    """

    with open(nome_arquivo, "w", newline="") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=dados.keys())
        escritor.writeheader()
        for i in range(len(dados["nome_produto"])):
            escritor.writerow({
                "nome_produto": dados["nome_produto"][i],
                "preco": dados["preco"][i],
                "quantidade": dados["quantidade"][i]
            })

# Gera os dados falsos
#dados_falsos = gerar_dados_falsos()

# Cria o arquivo CSV
#criar_arquivo_csv(dados_falsos)


# Lê o arquivo CSV e imprime os dados
with open("add.csv", "r") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        print(f"Nome do Produto: {linha['nome_produto']}, Preço: {linha['preco']}, Quantidade: {linha['quantidade']}")