"""
Exemplos de uso de dunder methods para definir operadores
"""

class Ponto:
    def __init__(self,x: int, y: int, z: int) -> None:
        self.__x = x
        self.__y = y
        self.__z = z
        
    @property
    def x(self): return self.__x
    
    @property
    def y(self): return self.__y
    
    @property
    def z(self): return self.__z
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(x={self.x!r}, y={self.y!r}, z={self.z!r})'
    
    def __add__(self, other):
        novo_x = self.x +  other.x
        novo_y = self.y + other.y
        novo_z = self.z + other.z
        return Ponto(novo_x, novo_y, novo_z)
    
    def __eq__(self, other):
        return (self.x + self.y + self.z) == (other.x + other.y + other.z)
    
    
ponto_1 = Ponto(6, 6, 6)
ponto_2 = Ponto(3, 6, 9)
ponto_3 = ponto_1 + ponto_2

print(f'{ponto_1} é IGUAL a {ponto_2}? {ponto_1 == ponto_2}')
