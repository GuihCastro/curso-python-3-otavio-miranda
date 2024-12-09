"""
Variáveis Livres e `nonlocal`
Uma variável é chamada de livre quando:
    -> Não é definida dentro da função onde está sendo usada; mas
    -> é encontrada no escopo externo dessa função (escopo de uma função "pai" ou global).
A palavra-chave nonlocal é usada para declarar que uma variável pertence a um escopo não local, ou seja, o escopo de uma função "pai", mas não global.
"""


def counter(start=0):
    inner_counter = start
    
    def increment():
        nonlocal inner_counter
        inner_counter += 1
        return inner_counter
    
    return increment


count = counter()

print(count())
print(count())
print(count())
print(count())
print(count())
print(count())
