"""
Manipulando Estados dentro da Classe
"""

class Camera:
    def __init__(self, nome):
        self.nome = nome
        self.esta_ligada = False
        self.esta_filmando = False
        
    def ligar(self):
        if self.esta_ligada:
            print(f'{self.nome} JÁ está ligada...')
            return
        self.esta_ligada = not self.esta_ligada
        print(f'Ligando {self.nome}...')
        
    def desligar(self):
        if not self.esta_ligada:
            print(f'{self.nome} JÁ está desligada...')
            return
        if self.esta_filmando:
            print('Não é possível desligar enquanto filma...')
            return
        self.esta_ligada = not self.esta_ligada
        print(f'{self.nome} foi desligada!')
        
    def fotografar(self):
        if not self.esta_ligada:
            print('Não é possível fotografar com a câmera desligada...')
            return
        if self.esta_filmando:
            print('Não é possível fotografar com a câmera filmando...')
            return
        print(f'Fotografia tirada com {self.nome}!')
        
    def filmar(self):
        if not self.esta_ligada:
            print('Não é possível filmar com a câmera desligada...')
            return
        self.esta_filmando = not self.esta_filmando
        print(f'Filmando com {self.nome}...')
        
    def parar_de_filmar(self):
        if not self.esta_filmando:
            print(f'{self.nome} NÃO está filmando.')
            return
        self.esta_filmando = not self.esta_filmando
        print(f'{self.nome} parou de filmar!')
        
        
nikon = Camera('Nikon')
canon = Camera('Canon')

nikon.ligar()
nikon.fotografar()
nikon.filmar()
nikon.parar_de_filmar()
nikon.desligar()

canon.desligar()
canon.filmar()
canon.ligar()
canon.filmar()
canon.fotografar()
canon.desligar()
canon.parar_de_filmar()
canon.desligar()
