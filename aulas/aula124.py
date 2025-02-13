"""
Metaclasses 
    -> São o tipo das classes
    
EM PYTHON, TUDO É UM OBJETO (CLASSES TAMBÉM)
Então, qual é o tipo de uma classe? (type)
Um objeto é uma instância de uma classe
Uma classe é uma instância de type (type é uma metaclass)
type('Name', (Bases,), __dict__)

Ao criar uma classe, coisas ocorrem por padrão nessa ordem:
    -> `__new__` da metaclass é chamado e cria a nova classe
    -> `__call__` da metaclass é chamado com os argumentos e chama:
        -> `__new__` da class com os argumentos (cria a instância)
        -> `__init__` da class com os argumentos
    -> `__call__` da metaclass termina a execução

Métodos importantes da metaclass:
    -> `__new__`(mcs, name, bases, dct) (Cria a classe)
    -> `__call__`(cls, *args, **kwargs) (Cria e inicializa a instância)

    "Metaclasses são magias mais profundas do que 99% dos usuários
    deveriam se preocupar. Se você quer saber se precisa delas,
    não precisa (as pessoas que realmente precisam delas sabem
    com certeza que precisam delas e não precisam de uma explicação
    sobre o porquê)."
        — Tim Peters (CPython Core Developer)
"""

# herda de object
# class Foo: ...

Foo = type('Foo', (object, ), {})
foo = Foo()

print(f'{type(foo)=}')
print(f'{type(Foo)=}')
