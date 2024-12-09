"""
Generator expression.
"""

import sys

lista = [n for n in range(1000000)]
generator = (n for n in range(1000000))

print(f'{sys.getsizeof(lista)=}\n{sys.getsizeof(generator)=}')

print()
for n in generator:
    if n > 100:
        break
    print(n)
print(n)
