"""
Exibir os índices de uma lista de nomes (sem usar o enumerate)
"""

lista = ['Gui', 'Mari', 'Maggie', 'Kurt', 'Guts', 'Red']
# i = 0

# for nome in lista:
#     print(f'{i}: {nome}')
#     i += 1

for i in range(len(lista)):
    print(f'{i}: {lista[i]}')
