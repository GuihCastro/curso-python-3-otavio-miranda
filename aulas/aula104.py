"""
Relações entre classes: associação, agregação e composição
    -> Associação
        |-> palavra-chave: "usa"
            |-> ex.: escritor USA caneta
    
Associação é um tipo de relação onde dois ou mais objetos estão ligados dentro do sistema.
Essa é a relação mais comum entre objetos e tem subconjuntos como agregação e composição.
Geralmente, temos uma associação quando um objeto tem um atributo que referencia outro objeto.
A associação não especifica como um objeto controla o ciclo de vida de outro objeto.
"""

class Escritor:
    def __init__(self, nome):
        self.__NOME = nome
        self.__ferramenta = None
         
    @property
    def nome(self):
        return self.__NOME
        
    @property
    def ferramenta(self):
        return self.__ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta
        
    def escrever(self):
        print(f'{self.nome} está escrevendo com {self.ferramenta.nome}')
        
        
class Ferramenta:
    def __init__(self, nome):
        self.__NOME = nome
        
    @property
    def nome(self):
        return self.__NOME
    
    def escrever(self):
        print(f'{self.nome} está escrevendo...')
        
        
guilherme = Escritor('Guilherme')
caneta = Ferramenta('Bic')

guilherme.ferramenta = caneta
guilherme.escrever()

guilherme.ferramenta = maquina_de_escrever = Ferramenta('Remington')
guilherme.escrever()

caneta.escrever()
maquina_de_escrever.escrever()
    