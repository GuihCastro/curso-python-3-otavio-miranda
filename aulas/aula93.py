"""
Introdução à POO em Python
`class` - Classes são moldes para criar novos objetos
As classes geram novos objetos (instâncias) que podem ter seus próprios atributos e métodos.
Os objetos gerados pela classe podem usar seus dados internos para realizar várias ações.
Por convenção, usamos PascalCase para nomes de classes.
"""


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


gui = Pessoa('Guilherme', 'Henrique de Castro')
mari = Pessoa('Mariana', 'Livraes Moura Fernandes')

print(f'{gui.nome=} | {gui.sobrenome=}')
print(f'{mari.nome=} | {mari.sobrenome=}')
