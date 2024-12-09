"""
Funções Decoradoras e Decoradores.
Uma função decoradora é uma função que recebe outra função como entrada e retorna uma nova função como saída.
Decoradores são uma forma elegante de adicionar ou modificar o comportamento de uma função ou método sem alterar seu código diretamente.
A sintaxe `@meu_decorador` é uma maneira mais conveniente de aplicar um decorador a uma função.
"""

def meu_decorador(func):
    def func_decorada(nome, msg=''):
        print('=' * 30)
        func(nome, msg)
        print('=' * 30)
    return func_decorada


@meu_decorador
def saudar(nome, msg):
    print(f'Olá, {nome}! {msg}')
    

dar_boas_vindas = saudar

dar_boas_vindas('Guilherme', 'Seja bem-vindo!')
