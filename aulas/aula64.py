"""
List comprehension com mais de um for
"""

# matriz = []
# for x in range(3):
#     for y in range(3):
#         lista.append((x, y))

matriz = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

print(f'{matriz=}')
