"""
Context Manager com classes - Criando e Usando gerenciadores de contexto

Podemos criar nossos próprios protocolos apenas implementando os dunder methods que o Python vai usar.
Isso é chamado de Duck typing. Um conceito relacionado com tipagem dinâmica onde o Python não está interessado no tipo em si do objeto, mas se alguns métodos existem nele para que ele funcione de forma adequada.

    Duck Typing:
    -> Quando vejo um pássaro que caminha como um pato, nada comoum pato e grasna como um pato, eu chamo aquele pássaro de pato.
    
Para criar um context manager, os métodos `__enter__` e `__exit__` devem ser implementados.
O método `__exit__` receberá a classe de exceção, a exceção e o traceback. Se ele retornar `True`, exceções no with serão suprimidas.

    Ex:
    with open('aula149.txt', 'w') as arquivo:
        ...
"""

class MyOpen:
    def __init__(self, caminho: str, modo: str) -> None:
        self.__caminho = caminho
        self.__modo = modo
        self.__arquivo = None
        
    @property
    def caminho(self): return self.__caminho
    
    @caminho.setter
    def caminho(self, novo_caminho): self.__caminho = novo_caminho
    
    @property
    def modo(self): return self.__modo
    
    @modo.setter
    def modo(self, novo_modo): self.__modo = novo_modo
    
    @property
    def arquivo(self): return self.__arquivo
    
    def __enter__(self):
        print('Abrindo arquivo...')
        self.__arquivo = open(self.caminho, self.modo, encoding='utf-8')
        return self.arquivo
    
    def __exit__(self, exception_, exception_class, traceback_):
        print('Fechando arquivo...')
        self.arquivo.close()
        
        
with MyOpen('.\\aulas\\aula118.txt', 'w') as arquivo:
    print('Dentro do WITH...')
    arquivo.write('Linha1\n')
    arquivo.write('Linha2\n')
    arquivo.write('Linha3\n')
