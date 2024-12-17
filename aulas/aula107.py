"""
Herança, Generalização e Especialização

Herança simples -> Relações entre classes
    Associação -> usa
    Agregação -> tem
    Composição -> É composto por
    Herança -> É um

Herança vs Composição

Classe principal (Pessoa)
  -> super class, parent class, base class
Classes filhas (Cliente)
  -> sub class, child class, derived class
"""

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
    
    def apresentar_se(self):
        print(f'Olá! Meu nome é {self.nome} {self.sobrenome}. Sou um(a) {self.__class__.__name__} e meu cpf é {self.cpf}')
        
        
class Cliente(Pessoa):
    __cpf = '123456'
    
    @property
    def cpf(self):
        return self.__cpf
    
    
class Aluno(Pessoa):
    def apresentar_se(self):
        print(f'Me chamo {self.nome} {self.sobrenome}, sou {self.__class__.__name__}, meu cpf é {self.cpf} e eu apresento assim')
        
        
cliente = Cliente('Dagon', 'da Silva')
aluno = Aluno('Cthulhu', 'dos Santos')

cliente.apresentar_se()
aluno.apresentar_se()
