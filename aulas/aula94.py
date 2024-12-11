"""
Métodos em instâncias de classes Python
"""


class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        print(f'{self.modelo} está acelerando...')


civic = Carro('Honda', 'Civic')
lancer = Carro('Mitsubishi', 'Lancer')

civic.acelerar()
lancer.acelerar()
