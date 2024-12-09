"""
Exercício 1: Dobrar Preços
Você recebeu uma lista com os preços de produtos. Use uma função lambda com map para dobrar os preços e exibir a nova lista.

    Entrada: [10, 20, 30, 40]
    Saída esperada: [20, 40, 60, 80]
"""

prices = [10, 20, 30, 40, 50]
double = list(map(lambda price: price*2, prices))

print(f'{double=}')
