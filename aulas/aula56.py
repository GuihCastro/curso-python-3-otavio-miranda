"""
Sets são eficientes para remover valores duplicados de outros iteráveis.
    -> Seus valores são sempre únicos;
    -> Não aceitam valores mutáveis; e também:
        -> Não tem índices;
        -> Não garantem ordem;
        -> São iteráveis (permitem o uso de for, in, not in, etc.).
"""

lista = [1, 2, 3, 4, 5, 6, 6, 6, 7, 8, 9, 10]

print(f'{lista=}')

conjunto = set(lista)
lista = list(conjunto)

print(f'{lista=}')
print(6 in conjunto)
for numero in conjunto:
    print(f'{numero=}')
