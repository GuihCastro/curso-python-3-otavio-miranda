"""
Herança Múltipla - Python Orientado a Objetos

Quer dizer que no Python, uma classe pode estender mais de uma classe ao mesmo tempo.

Herança simples:
    Animal -> Mamifero -> Humano -> Pessoa -> Cliente
Herança múltipla e mixins:
    Log -> FileLog
    Animal -> Mamifero -> Humano -> Pessoa -> Cliente
    Cliente(Pessoa, FileLog)

A, B, C, D
D(B, C) - C(A) - B(A) - A

método -> falar
          A
        /   \
       B     C
        \   /
          D

Python 3 usa C3 superclass linearizationpara gerar o mro.
https://en.wikipedia.org/wiki/C3_linearization

Para saber a ordem de chamada dos métodos podemos usar:
    o método de classe `Classe.mro()`;
    ou o atributo `__mro__` (Dunder - Double Underscore)
"""

class A:
    ...
    
    def method(self):
        print('A')
        
        
class B(A):
    ...
    
    def method(self):
        print('B')
        
        
class C(A):
    ...
    
    def method(self):
        print('C')
        
        
class D(B, C):
    ...
    
    def method(self):
        print('D')
        
       
print(D.__mro__) # mostra o caminho de execução
        
d = D()
d.method()
