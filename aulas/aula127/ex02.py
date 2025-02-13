#typing.NamedTuple

from typing import NamedTuple

class Card(NamedTuple):
    rank: str
    suit: str
    
ace_of_spades = Card('A', '♠')

print(ace_of_spades)
