"""
Listas em Python
Tipo list -> Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis -> índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
Lista vazia ([]) resulta em um bool Falsy
"""

lista = [123, True, 'Guilherme', 1.2, []]

print(lista)
print(lista[2], type(lista[2]))

lista[2] = 'Mariana'

print(lista)
print(lista[2], type(lista[2]))
