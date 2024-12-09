"""
Higher Order Functions | Funções de Ordem Superior
São funções que podem:
    -> Receber outra(s) função(ões) como argumento(s); e/ou
    -> Retornar outra(s) função(ões) como resultado. 
"""


def greeting(msg, name):
    return f'{msg}, {name}!'


def run(func, *args):
    return func(*args)


greetings = greeting

print(run(greetings, 'Bom dia', 'Guilherme'))
print(run(greetings, 'Boa noite', 'Mariana'))
