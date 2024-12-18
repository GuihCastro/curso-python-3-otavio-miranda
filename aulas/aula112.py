"""
`@abstractmethod` para qualquer método já decorado (`@property`, `@property.setter`, etc)
É possível criar `@property`, `@property.setter`, `@classmethod`, `@staticmethod` e métodos normais como abstratos
Para isso, usamos o decorador `@abstractmethod` como decorator mais interno.
    
    * `Foo` e `Bar` são palavras usadas como placeholder para palavras que podem mudar na programação.
"""

from abc import ABC, abstractmethod


class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = None
        self.name = name
        
    @property
    def name(self): return self._name
    
    @name.setter
    @abstractmethod
    def name(self): ...
    
    
class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
        
    @AbstractFoo.name.setter
    def name(self, name): self._name = name
    
    
foo = Foo('Bar')
print(foo.name)
    