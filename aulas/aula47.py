"""
args -> Argumentos não nomeados
* (*args) -> empacotamento e desempacotamento
    Lembrete de desempacotamento:
        x, y, *_ = 1, 2, 3, 4, 5, 6
"""


def soma(*args):
    resultado = 0
    for num in args:
        resultado += num
    return resultado


numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

soma1 = soma(6, 6, 6)
soma2 = soma(1, 2, 3, 4, 5, 6)
soma3 = soma(*numeros)

print(soma1)
print(soma2)
print(soma3)
