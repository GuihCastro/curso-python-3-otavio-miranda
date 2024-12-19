"""
Python Dunder Methods (Dunder = Double Underscore = `__dunder__`)
    -> Exemplos com `__repr__` e `__str__`

Antigo e útil: https://rszalski.github.io/magicmethods/
https://docs.python.org/3/reference/datamodel.html#specialnames

    __lt__(self,other) - self < other
    __le__(self,other) - self <= other
    __gt__(self,other) - self > other
    __ge__(self,other) - self >= other
    __eq__(self,other) - self == other
    __ne__(self,other) - self != other
    __add__(self,other) - self + other
    __sub__(self,other) - self - other
    __mul__(self,other) - self * other
    __truediv__(self,other) - self / other
    __neg__(self) - -self
    __str__(self) - str
    __repr__(self) - str
"""

class CoordenadaCartesiana:
    def __init__(self,x: int, y: int, z: str) -> None:
        self.__x = x
        self.__y = y
        self.__z = z
        
    @property
    def x(self): return self.__x
    
    @property
    def y(self): return self.__y
    
    @property
    def z(self): return self.__z
    
    def __str__(self) -> str:
        return f'Atributos de {self.__class__.__name__}: {self.x}, {self.y} e {self.z}'
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(x={self.x!r}, y={self.y!r}, z={self.z!r})'
    
    
coord1 = CoordenadaCartesiana(3, 6, 'Algum ponto')
coord2 = CoordenadaCartesiana(6, 6, '6')

print(coord1)
print(f'{coord1!r}')
print(coord2)
print(f'{coord2!r}')
    