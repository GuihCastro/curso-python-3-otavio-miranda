"""
Escopo de classe e de métodos
"""

class Animal:
    def __init__(self, nome):
        self.nome = nome
        
    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}'
    
    def comer(self, *args):
        return self.comendo(*args)
    

leao = Animal('Leão')
print(leao.comer('churrasco'))
