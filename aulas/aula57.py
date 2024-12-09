"""
Métodos úteis de Sets
add, update, clear, discard -> (CRUD)
"""

conjunto = set()

conjunto.add(1)
conjunto.add(2)

print(f'{conjunto=}')

conjunto.update(('Guilherme',))

print(f'{conjunto=}')

conjunto.discard('Guilherme')

print(f'{conjunto=}')

conjunto.clear()

print(f'{conjunto=}')
