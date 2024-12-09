"""
Aumente os preços dos produtos na lista em 10%.
Gere novos_produtos por deep copy (cópia profunda)
"""

from copy import deepcopy

from dados import produtos

novos_produtos = [{**produto, 'preco': round(produto['preco']*1.1, 2)} for produto in deepcopy(produtos)]

print(*novos_produtos, sep='\n')
