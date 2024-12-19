"""
Método especial `__call__`

"callable" é algo que pode ser executado (chamado) com parênteses
Em classes normais, `__call__` faz a instância de uma classe "callable".
"""

class Call:
    def __init__(self, phone: str) -> None:
        self.__phone = phone
        
    @property
    def phone(self): return self.__phone
    
    def __call__(self, name):
        print(f'{name} está chamando {self.phone}')
        return True
    
    
call = Call('666')
print(call('Dagon'))
