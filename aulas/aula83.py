"""
`count()` -> iterador infinito do `itertools`
"""

from itertools import count

for i in count(start=6, step=6):
    if i > 666:
        break
    print(i)
