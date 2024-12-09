"""
`filter()`
Semelhante ao `map()`, recebe como argumentos:
    1 -> uma função que filtrará os elemtos de um iterável
    2 -> o iterável que terá seus elementos filtrados pela função
Ao final, retorna um novo iterável com os valores filtrados
"""

def print_iter(titulo, iterator):
    print(f'{titulo}', *iterator, sep='\n',end='\n\n')
    
    
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

produtos_custando_vinte_ou_mais = filter(lambda produto: produto['preco']>=20, produtos)

print_iter('Produtos:', produtos)
print_iter('Produtos acima de R$20.00:', produtos_custando_vinte_ou_mais)
