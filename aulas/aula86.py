"""
`map()` e `partial()`
O `map()` recebe como argumentos:
    1 -> uma função que processará os elemtos de um iterável
    2 -> o iterável que terá seus elementos processados pela função
Ao final, retorna um iterador com os valores processados

O `partial()` atua como uma Higher Order Function, recebendo uma função e um ou mais de seus parâmetros como argumentos (closure)
"""

from functools import partial


def aumentar_porcentagem(valor, incremento):
    return round(valor * incremento, 2)


# exemplo de `partial()`
aumentar_dez_porcento = partial(aumentar_porcentagem, incremento=1.1)


def mudar_preco(produto):
    return {**produto, 'preco': aumentar_dez_porcento(produto['preco'])}


def print_iter(titulo, iterator):
    print(f'{titulo}', *iterator, sep='\n',end='\n\n')


# exemplo simples de `map()`
lista_triplicada = list(map(lambda n: n*3, [1, 2, 3, 4]))
print(f'{lista_triplicada=}', end='\n\n') 

# exemplo mais complexo -> alterando preços de produtos (dicionários) em uma lista
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

produtos_encarecidos = list(map(mudar_preco, produtos))

print_iter('Produtos:', produtos)
print_iter('Produtos encarecidos:', produtos_encarecidos)
