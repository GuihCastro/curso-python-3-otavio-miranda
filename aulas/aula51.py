"""
CRUD com dicionários
"""

pessoa = {}
chave_1 = 'nome'
chave_2 = 'sobrenome'
chave_3 = 'idade'
chave_4 = 'altura'

pessoa[chave_1] = 'Guilherme'
pessoa[chave_2] = 'Henrique de Castro'
pessoa[chave_3] = 32
pessoa[chave_4] = 1.69

print(f'{pessoa = }')
print(f'{pessoa['nome']} tem {pessoa['idade']} anos.') 

pessoa['nome'] = 'Mariana'
pessoa[chave_2] = 'Livraes Moura Fernandes'

print(f'{pessoa = }')

del pessoa[chave_4]

print(f'{pessoa = }')

if pessoa.get('altura') is not None and pessoa.get('nome') is not None:
    print(f'{pessoa['nome']} tem {pessoa['altura']} de altura')
else:
    print('A(s) chave(s) "nome" e/ou "altura" não existe(m)')
