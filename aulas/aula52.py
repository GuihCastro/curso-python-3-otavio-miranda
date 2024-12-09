"""
Métodos úteis de dicionários em Python - pt. 1
    -> len - retorna a quantidade de chaves (podemos usar `len(dict)` ou `dict.__len__()`);
    -> keys - retorna um iterável com as chaves;
    -> values - retorna um iterável com os valores;
    -> items - retorna um iterável com tuplas formadas por chaves e valores;
    -> setdefault - cria uma chave caso ela não exista, mas não sobrescreve caso exista;
"""

pessoa = {
    'nome': 'Guilherme',
    'sobrenome': 'Henrique de Castro',
}

print(f'{pessoa=}')

tamanho = len(pessoa)
print(f'{tamanho=}')
chaves = list(pessoa.keys())
print(f'{chaves=}')
valores = list(pessoa.values())
print(f'{valores=}')
itens = list(pessoa.items())
print(f'{itens=}')

pessoa.setdefault('idade', 666)

print(f'{pessoa=}')

# iterando
print('\nITERANDO CHAVES')
for chave in pessoa.keys():
    print(f'{chave=}')
    
print('\nITERANDO VALORES')
for valor in pessoa.values():
    print(f'{valor=}')
    
print('\nITERANDO ITENS')
for chave, valor in pessoa.items():
    print(f'Item = {chave=}: {valor=}')
