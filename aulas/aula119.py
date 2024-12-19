"""
Tratando exceções em Context Manager com classes
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
    
    def __exit__(self, exception_class, exception_, traceback_):
        print('Fechando arquivo...')
        self.arquivo.close()
        
        # print(f'{exception_class}: {exception_} -> {traceback_}')
        
        exception_.add_note('Minha nota para a exceção...')
        
        # return True # suprime qualquer exceção que ocorra no with
        
        
with MyOpen('.\\aulas\\aula119.txt', 'w') as arquivo:
    print('Dentro do WITH...')
    arquivo.write('Linha1\n')
    arquivo.write('Linha2\n', 123)
    arquivo.write('Linha3\n')
