"""
Exemplificando a criação de uma Metaclasse
"""

def my_repr(self):
    return f'{self.__class__.__name__}({self.__dict__})'


# metaclasses herdam de `type`
class Meta(type):
    def __new__(mcs, name, bases, dct):
        print('NEW da METACLASSE')
        cls = super().__new__(mcs, name, bases, dct)
        cls.attr = 666
        cls.__repr__ = my_repr
        
        if 'speak' not in cls.__dict__ or not callable(cls.__dict__['speak']):
            raise NotImplementedError('Implemente o método `speak`')
        
        return cls
    
    def __call__(self, *args, **kwds):
        instance =  super().__call__(*args, **kwds)
        
        if 'name' not in instance.__dict__:
            raise NotImplementedError('Crie o atributo `name`')
        
        return instance


# a metaclasse entra como argumento da classe
class Person(metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print('NEW da CLASSE')
        instance = super().__new__(cls)
        return instance
    
    def __init__(self, name):
        print('INIT da CLASSE')
        self.name = name
        
    def speak(self): print('Falando...')
    
    
gui = Person('Guilherme')
print(f'{gui=}')
print(f'{gui.attr=}')
gui.speak()
