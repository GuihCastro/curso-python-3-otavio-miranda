"""
Funções decoradoras e decoradores com MÉTODOS
"""


def add_repr(cls: super) -> object:
    def repr(self: object) -> str:
        return f'{self.__class__.__name__}({self.__dict__})'
    cls.__repr__ = repr
    return cls


def my_location(method):
    def inner(self, *args, **kwargs) -> str:
        location = method(self, *args, **kwargs)
        response = f'Você está em {location}.'
        if location == 'Marte':
            response += ' Aqui é a sua verdadeira casa!'
        return response
    return inner


@add_repr
class Country:
    def __init__(self, name: str) -> None:
        self.name = name

    @my_location
    def get_location(self): return self.name


@add_repr
class Planet:
    def __init__(self, name: str) -> None:
        self.name = name

    @my_location
    def get_location(self): return self.name


brasil = Country('Brasil')
china = Country('China')
terra = Planet('Terra')
marte = Planet('Marte')

print(brasil)
print(china)
print(terra)
print(marte)

print(brasil.get_location())
print(china.get_location())
print(terra.get_location())
print(marte.get_location())
