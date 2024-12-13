"""
Métodos de classe (@classmethod) + Factories (fábricas)
    -> Métodos de classe são métodos onde "self" será substituído por "cls", ou seja, ao invés de receber a
    instância no primeiro parâmetro, receberá a própria classe
"""

class Pessoa:
    sobrenome = 'Henrique de Castro Livraes' # atributo de classe
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    @classmethod
    def criar_com_32_anos(cls, nome): # factory method
        return cls(nome, 32)
    
    
gui = Pessoa.criar_com_32_anos('Guilherme')
mari = Pessoa.criar_com_32_anos('Mariana')
