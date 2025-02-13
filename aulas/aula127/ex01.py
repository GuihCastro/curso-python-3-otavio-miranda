"""Named Tuples 

São tuplas imutáveis com nomes para valores

Usamos namedtuples para criar classes de objetos que sejam apenas um agrupamento de atributos, como classes normais sem métodos, ou registros de bases de dados, etc.

As namedtuples são imutáveis assim como as tuplas.

    * https://docs.python.org/3/library/collections.html#collections.namedtuple
    * https://docs.python.org/3/library/typing.html#typing.NamedTuple
"""

# colletions.namedtuple()
from collections import namedtuple

Card = namedtuple('Card', ['rank', 'suit'])

ace_of_spades = Card('A', '♠')

print(ace_of_spades)
