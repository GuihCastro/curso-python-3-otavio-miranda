"""
`super()` e a sobreposição de métodos
"""

# class MyStr(str):
#     def upper(self):
#         print('Chamando o método upper...')
#         return super().upper()
    
    
# palavra = MyStr('Palavra')
# print(f'{palavra=}')
# print(f'{palavra.upper()=}')

class Pessoa:
    __cpf = 'não tem'
    
    def __init__(self, nome, sobrenome):
        self.__nome = nome
        self.__sobrenome = sobrenome
        
    @property
    def cpf(self):
        return self.__cpf
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def sobrenome(self):
        return self.__sobrenome
    
    def apresentar_se(self, end='\n'):
        print(f'Olá! Meu nome é {self.nome} {self.sobrenome}. Sou um(a) {self.__class__.__name__} e meu cpf é {self.cpf}', end=end)
        
        
class Cliente(Pessoa):
    __cpf = '123456'
    
    def __init__(self, nome, sobrenome, codigo):
        super().__init__(nome, sobrenome)
        self.__codigo = codigo
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, novo_codigo):
        self.__codigo = novo_codigo
        
    def apresentar_se(self, *args, **kwargs):
        super().apresentar_se(*args, **kwargs)
        print(f'Meu código é: {self.codigo}')

    
    
class Aluno(Pessoa):
    def apresentar_se(self):
        print(f'Me chamo {self.nome} {self.sobrenome}, sou {self.__class__.__name__}, meu cpf é {self.cpf} e eu me apresento assim')
        
        
cliente = Cliente('Dagon', 'da Silva', 666)
aluno = Aluno('Cthulhu', 'dos Santos')

aluno.apresentar_se()
cliente.apresentar_se(end=' | ')
