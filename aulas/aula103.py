"""
Encapsulamento (modificadores de acesso: public, protected, private)
Python NÃO TEM modificadores de acesso, mas podemos seguir as seguintes convenções para nomear os atrbutos e métodos:

    (sem underline) = public
        -> Pode ser usado em qualquer lugar.
    `_` (um underline) = protected
        -> Deve ser usado APENAS na classe em que foi declarado ou suas subclasses.
    `__` (dois underlines) = private
        -> Deve ser usado APENAS na classe em que foi declarado.
        -> Apesar de não impedir de fato seu uso fora do escopo correto, o Python faz "name mangling" (desfiguração de nomes) formatando como `_NomeClasse__nome_attr_ou_method`.
"""

class Modifiers:
    def __init__(self):
        self.public = 'Atributo público' # pode ser usado em qualquer lugar
        self._protected = 'Atributo protegido' # NÃO DEVE ser usado fora da classe ou suas subclasses
        self.__private = 'Atributo privado' # NÃO DEVE ser usado fora da classe
        
    def public_method(): # pode ser usado em qualquer lugar
        return 'Método público'
    
    def _protected_method(): # NÃO DEVE ser usado fora da classe ou suas subclasses
        return 'Método protegido'
        
    def __private_method(): # NÃO DEVE ser usado fora da classe
        return 'Método privado'
    
    
obj = Modifiers()
obj.public # correto
obj.public_method() # correto
obj._protected # errado
obj._protected_method # errado
obj.__private # errado
obj.__private_method # errado, e gera erro devido ao "name mangling" -> `__Modifiers_private_method`
