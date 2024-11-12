from django.shortcuts import render
import csv
# Create your views here.

with open("add.csv", "r") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        print(f"Nome do Produto: {linha['nome_produto']}, Preço: {linha['preco']}, Quantidade: {linha['quantidade']}")

def index(requests):
    context = leitor
    return (render, 'index.html', context)