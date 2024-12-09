"""
Ordene os produtos por nome decrescente (do maior para o menor)
Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
"""

from copy import deepcopy

from dados import produtos

# produtos = sorted(produtos, key=lambda produto: produto['nome'], reverse=True)
produtos_ordenados_por_nome = sorted(deepcopy(produtos), key=lambda produto: produto['nome'], reverse=True)

print(*produtos_ordenados_por_nome, sep='\n')
