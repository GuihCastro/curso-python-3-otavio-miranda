from log import LogFileMixin

class Eletronico:
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo
        self.__ligado = False
        
    @property
    def marca(self):
        return self.__marca
    
    @property
    def modelo(self):
        return self.__modelo
    
    @property
    def ligado(self):
        return self.__ligado
    
    @ligado.setter
    def ligado(self, estado: bool):
        self.__ligado = estado
    
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            
    def desligar(self):
        if self.ligado:
            self.ligado = False
            
            
class Smartphone(Eletronico, LogFileMixin):
    def ligar(self):
        if not self.ligado:
            self._log_success(f'{self.marca} {self.modelo} foi ligado!')
            return super().ligar()
        self._log_error(f'Tentou ligar {self.marca} {self.modelo} enquanto já estava ligado...')
        
    def desligar(self):
        if self.ligado:
            self._log_success(f'{self.marca} {self.modelo} foi desligado!')
            return super().desligar()
        self._log_error(f'Tentou desligar {self.marca} {self.modelo} enquanto já estava desligado...')
