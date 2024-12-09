"""
Ordene os produtos por preço crescente (do menor para o maior)
Gere produtos_ordenados_por_preco por deep coppy (cópia profunda)
"""

from copy import deepcopy

from dados import produtos

produtos_ordenados_por_preco = sorted(deepcopy(produtos), key=lambda produto: produto['preco'])

print(*produtos_ordenados_por_preco, sep='\n')
