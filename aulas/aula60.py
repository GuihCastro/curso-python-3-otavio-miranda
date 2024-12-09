"""
Empacotamento e desempacotamento de dicionários (**kwargs)
"""


def mostrar_argumentos_nomeados(*args, **kwargs):
    print(f'NÃO NOMEADOS: {args}')
    
    print('NOMEADOS:')
    for chave, valor in kwargs.items():
        print(f'{chave=}: {valor=}')


pessoa = {
    'nome': 'Mariana',
    'sobrenome': 'Livraes Moura Fernandes',
}

dados = {
    'idade': 32,
    'altura': 1.65,
}

pessoa_com_dados = {**pessoa, **dados}

print(f'{pessoa=}\n{dados=}\n{pessoa_com_dados=}\n')

config = {
    'chave_1': 1,
    'chave_2': 2,
    'chave_3': 3,
}

mostrar_argumentos_nomeados(**config)
