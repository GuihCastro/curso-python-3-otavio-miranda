"""
Filtro de dados em list comprehension (filter)
"""

lista = [n for n in range(10)]

print(f'{lista=}')

nova_lista = [num for num in lista if num % 3 == 0]

print(f'{nova_lista=}')

produtos = [
    {'nome': 'produto 1', 'preco': 20, },
    {'nome': 'produto 2', 'preco': 10, },
    {'nome': 'produto 3', 'preco': 30, },
]

print(*produtos, sep='\n')

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} if produto['preco'] > 20 else {**produto} # map
    for produto in produtos
    if produto['preco'] >= 20 # filter 
]

print()
print(*novos_produtos, sep='\n')
