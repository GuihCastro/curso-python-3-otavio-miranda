"""
Funções decoradoras e decoradores com CLASSES
"""

def add_repr(cls: super) -> object:
    def repr(self: object) -> str:
        return f'{self.__class__.__name__}({self.__dict__})'
    cls.__repr__ = repr
    return cls


@add_repr
class Country:
    def __init__(self, name: str) -> None:
        self.name = name
        
    # @property
    # def name(self): return self.__name
    
    
@add_repr
class Planet:
    def __init__(self, name: str) -> None:
        self.name = name
        
    # @property
    # def name(self): return self.__name
    
    
brasil = Country('Brasil')
china = Country('China')
terra = Planet('Terra')
marte = Planet('Marte')

print(brasil)
print(china)
print(terra)
print(marte)
