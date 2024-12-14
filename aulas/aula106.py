"""
Relações entre classes: associação, agregação e composição
    -> Composição 

É uma especialização da agregação, mas nela, quando o objeto "pai" for apagado, todas as referências dos objetos filhos também são apagadas.
"""

class Cliente:
    def __init__(self, nome):
        self.__nome = nome
        self.__enderecos = []
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def enderecos(self):
        return self.__enderecos
    
    def adicionar_endereco(self, rua, numero):
        self.__enderecos.append(Endereco(rua, numero)) # o objeto filho é criado dentro do objeto pai
        
    def adicionar_endereco_externo(self, endereco):
        self.__enderecos.append(endereco) # agregação
        
    def listar_enderecos(self):
        print(f'Endereços de {self.nome}:')
        for endereco in self.enderecos: print(f'{endereco.rua}, {endereco.numero}')
        
    def __del__(self):
        print(f'Deletando cliente {self.nome}...')
        
        
class Endereco:
    def __init__(self, rua, numero):
        self.__rua = rua
        self.__numero = numero
        
    @property
    def rua(self):
        return self.__rua
    
    @rua.setter
    def rua(self, nova_rua):
        self.__rua = nova_rua
    
    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, novo_numero):
        self.__numero = novo_numero
        
        
cliente_1 = Cliente('Guilherme')
cliente_1.adicionar_endereco('Rua tal', 666) # composição | será deletado junto do cliente

endereco = Endereco('Rua tal e tal', 6) # agregação | não será deletado com o cliente
cliente_1.adicionar_endereco_externo(endereco)

cliente_1.listar_enderecos()

del cliente_1

print(f'{endereco.rua}, {endereco.numero} ainda existe!')
