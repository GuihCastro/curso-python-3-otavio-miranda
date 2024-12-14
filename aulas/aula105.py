"""
Relações entre classes: associação, agregação e composição
    -> Agregação 
        |-> palavra-chave "tem", ex.: carro TEM rodas
            
É uma forma mais especializada de associaçãoentre dois ou mais objetos. 
Cada objeto terá seu ciclo de vida independente.
Geralmente é uma relação de um para muitos, onde um objeto tem um ou muitos objetos.
Os objetos podem viver separadamente, mas pode se tratar de uma relação onde um objeto precisa de outro para fazer determinada tarefa.
*(existem controvérsias sobre as definições de agregação).*
"""

class CarrinhoDeCompras:
    def __init__(self):
        self.__produtos = []
        
    def adicionar_produtos(self, *produtos):
        for produto in produtos: 
            self.__produtos.append(produto)
            print(f'{produto.nome} adicionado ao carrinho!')
            
    def listar_produtos(self):
        print('Produtos no carrinho:')
        for produto in self.__produtos: print(f'{produto.nome} -> R${produto.preco:.2f}')

    def calcular_total(self):
        total = sum([produto.preco for produto in self.__produtos])
        return total
        
        
class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
        
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, novo_preco):
        self.__preco = novo_preco
        
    
carrinho = CarrinhoDeCompras()
zero_red, moondrop_may = Produto('Fone IEM Truthear ZERO:Red', 599.99), Produto('Fone IEM Moondrop May', 710.00)

carrinho.adicionar_produtos(zero_red, moondrop_may)
carrinho.listar_produtos()
print(f'Valor total: R${carrinho.calcular_total():.2f}')
        