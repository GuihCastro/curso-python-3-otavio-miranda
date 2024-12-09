"""
`combinations()`, `permutations()` e `product()` -> `itertools`
"""

from itertools import permutations, combinations, product


def print_iter(iterator):
    print(*list(iterator), sep='\n', end='\n\n')
    
pessoas = ['Guilherme', 'Mariana', 'Maggie', 'Kurt', 'Guts', 'Red']
print_iter(combinations(pessoas, 2)) # combionations
print_iter(permutations(pessoas, 2)) # permutations

camisetas = [
    ('preta', 'branca'),
    ('masculina', 'feminina'),
    ('p', 'm', 'g'),
]
print_iter(product(*camisetas)) # product
