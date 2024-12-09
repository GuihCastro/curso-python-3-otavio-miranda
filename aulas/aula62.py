"""
Mapeamento de dados em list comprehension (map)
"""

produtos = [
    {'nome': 'produto 1', 'preco': 20, },
    {'nome': 'produto 2', 'preco': 10, },
    {'nome': 'produto 3', 'preco': 30, },
]

print(*produtos, sep='\n')

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else
    {**produto}
    for produto in produtos
]

print()
print(*novos_produtos, sep='\n')
