"""
Exercício 3: Ordenar Produtos por Preço
Você trabalha em um e-commerce e tem uma lista de produtos representados como tuplas (nome, preço). Use uma função lambda com sorted para ordenar os produtos pelo preço.

    Entrada: produtos = [("Celular", 1500), ("Notebook", 3000), ("Fone", 200), ("Monitor", 700)]
    Saída esperada: [('Fone', 200), ('Monitor', 700), ('Celular', 1500), ('Notebook', 3000)]
"""

products = [("Celular", 1500), ("Notebook", 3000), ("Fone", 200), ("Monitor", 700)]
sorted_products = sorted(products, key=lambda prod: prod[1])

print(f'{sorted_products=}')
