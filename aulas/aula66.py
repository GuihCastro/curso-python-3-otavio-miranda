"""
Método `isinstance()` - para checar se um objeto é de determinado tipo.
"""

lista = ['a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'nome': 'Guilherme'}]

for item in lista:
    if isinstance(item, set):
        print(f'SET:\n{item=}')
    elif isinstance(item, str):
        print(f'STR:\n{item=}, {item.upper()}')
    elif isinstance(item, (int, float)):
        print(f'NUM (INT ou FLOAT):\n{item=}, {item*2}')
    else:
        print(f'OUTRO:\n{item=}, {type(item)}')
