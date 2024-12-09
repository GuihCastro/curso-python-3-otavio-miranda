"""
Exercício - Unir listas

Crie uma função zipper (como o zipper de roupas)
O trabalho dessa função será unir duas
listas na ordem.
Use todos os valores da menor lista.

Ex.:
    ['Salvador', 'Ubatuba', 'Belo Horizonte']
    ['BA', 'SP', 'MG', 'RJ']
Resultado
    [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
"""

def zipper(lista_1, lista_2):
    lista_zip = [(lista_1[i], lista_2[i]) for i in range(min(len(lista_1), len(lista_2)))]
    return lista_zip


estados = ['Salvador', 'Ubatuba', 'Belo Horizonte']
siglas = ['BA', 'SP', 'MG', 'RJ']
estados_com_siglas = zipper(estados, siglas)

print(f'{estados_com_siglas=}')
