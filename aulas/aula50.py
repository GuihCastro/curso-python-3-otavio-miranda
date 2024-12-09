"""
Dicionários em Python
Dicionários são estruturas de dados do tipo "chave" e "valor".
Chaves podem ser consideradas como equivalentes aos "índices" de uma lista, podendo ser de qualquer um dos tipos imutáveis: str, int, float, bool, tuple, etc.
Os valores podem ser de qualquer tipo, mutável ou imutável, incluindo outro dicionário.
Usamos um par de chaves - {} - ou a classe `dict()` para criar um dicionário.
    -> Classes mutáveis: str, int, float, bool, tuple;
    -> Classes imutáveis: list, dict.
"""

# pessoa = dict(nome='Guilherme', sobrenome='Henrique de Castro')

pessoa = {
    'nome': 'Guilherme',
    'sobrenome': 'Henrique de Castro',
    'idade': 32,
    'altura': 1.69,
    'endereços': [
        {'rua': 'tal', 'número': 666},
        {'rua': 'tal e tal', 'número': 666},
    ]
}

print(f'{pessoa['nome']} tem {pessoa['idade']} anos.')
print()
# iterando sobre o dicionário
for chave in pessoa:
    print(f'{chave=}: valor={pessoa[chave]}')
