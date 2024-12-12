"""
Atributos de classe
    -> são aplicados a todas as instâncias da mesma
"""

class Familiar:
    FAMILY = 'Henrique de Castro Livraes'
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def get_full_name(self):
        return f'{self.name} {__class__.FAMILY}'
    

gui = Familiar('Guilherme', 32)
mari = Familiar('Mariana', 32)
maggie = Familiar('Maggie', 8)
kurt = Familiar('Kurt', 7)
guts = Familiar('Guts', 4)
red = Familiar('Red', 3)

print(gui.get_full_name())
print(mari.get_full_name())
print(maggie.get_full_name())
print(kurt.get_full_name())
print(guts.get_full_name())
print(red.get_full_name())
