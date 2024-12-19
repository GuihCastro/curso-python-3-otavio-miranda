"""
`__new__` e `__init__` em classes Python

`__new__` é o método responsável por criar e retornar o novo objeto. Por isso, recebe `cls` e não `self`.
    -> `__new__` ❗️DEVE retornar o novo objeto❗️
    -> Podemos usar o `__new__` para fazer coisas entre a criação e a inicialização da instância.
    
`__init__` é o método responsável por inicializar a instância. Por isso, recebe `self`.
    -> `__init__` ❗️NÃO DEVE retornar nada (None)❗️
    
    * `object` é a super classe de uma classe
"""

class Classe:
    def __new__(cls, *args, **kwargs):
        print('Criando a instância no `__new__`...')
        instancia = super().__new__(cls)
        print('Instância criada. retornando o `self` para o `__init__`...')
        return instancia
    
    def __init__(self, atr):
        self.__atr = atr
        
    @property
    def atr(self): return self.__atr
    
    def __repr__(self): return f'{self.__class__.__name__}({self.atr!r})'
    
    
objeto = Classe('atributo')
print(f'{objeto=}')
