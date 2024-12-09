"""
Métodos úteis de dicionários em Python - pt. 2
    -> get - obtém uma chave, ou retorna None (ou outro valor determinado como argumento) caso ela não exista;
    -> pop - apaga um item com base na chave especificada (similar ao del)
    -> popitem - apaga o último item;
    -> update - atualiza um dicionário com outro.
"""

pessoa = {
    'nome': 'Guilherme',
    'sobrenome': 'Henrique de Castro',
}

print(pessoa.get('nome'))
print(pessoa.get('idade'))

pessoa.update({
    'nome': 'Mariana',
    'idade': 32
})

pessoa.update(altura=1.65)

tupla = (('gênero', 'F'), ('profissão', 'ilustradora'))

pessoa.update(tupla)

print(f'{pessoa=}')

sobrenome = pessoa.pop('sobrenome')

print(f'{sobrenome=}')

ultimo_item = pessoa.popitem()

print(f'{ultimo_item=}')
print(f'{pessoa=}')
