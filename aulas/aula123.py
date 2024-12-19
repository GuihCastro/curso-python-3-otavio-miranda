"""
Classes decoradoras (Decorator Classes)
"""

class Multiplicar:
    def __init__(self, multiplicador):
        self.__multiplicador = multiplicador
        
    def __call__(self, func):
        def inner(*args, **kwargs):
            result = func(*args, **kwargs) * self.__multiplicador
            return result
        return inner


@Multiplicar(6)
def somar(*args): return sum(args)


print(somar(6, 6))
