"""
Dictionary Comprehension e Set Comprehension
"""

produto = {
    'nome': 'Caneta Azul',
    'preco': 2.50,
    'categoria': 'Escritório',
}

novo_produto = {
    chave: valor.lower() if isinstance(valor, str) else valor # map
    for chave, valor in produto.items()
    if chave != 'categoria' # filter
}

print(f'{novo_produto=}')

conjunto = {i * 2 for i in range(10)}

print(f'{conjunto=}')
