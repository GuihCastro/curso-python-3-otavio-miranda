"""
Exercício com classes

    * 1 -> Crie uma classe Carro (Nome)
    * 2 -> Crie uma classe Motor (Nome)
    * 3 -> Crie uma classe Fabricante (Nome)
    * 4 -> Faça a ligação entre Carro tem um Motor
        Obs.: Um motor pode ser de vários carros
    * 5 -> Faça a ligação entre Carro e um Fabricante
        Obs.: Um fabricante pode fabricar vários carros
    Exiba o nome do carro, motor e fabricante na tela
"""

class Fabricante:
    def __init__(self, nome):
        self.__nome = nome
        self.__carros = []
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
        
    @property
    def carros(self):
        return self.__carros
    
    def montar_carro(self, modelo, motor):
        print(f'Montando {self.nome} {modelo}...')
        carro = Carro(self.nome, modelo, motor)
        self.__carros.append(carro)
        return carro
        
    def listar_carros(self):
        print(f'Carros da {self.nome}:')
        for carro in self.carros: print(f'{carro.marca} {carro.modelo} {carro.motor.nome}')
    

class Carro:
    def __init__(self, marca, modelo, motor: object):
        self.__marca = marca
        self.__modelo = modelo
        self.__motor = motor
        
    @property
    def marca(self):
        return self.__marca
    
    @property
    def modelo(self):
        return self.__modelo
    
    @property
    def motor(self):
        return self.__motor
    
    @motor.setter
    def motor(self, novo_motor):
        self.__motor = novo_motor
        
    def colocar_motor(self, motor):
        self.motor = motor
        print(f'Motor {motor} colocado no {self.marca} {self.modelo}!')
        
    def acelerar(self):
        self.motor.ligar_motor()
        print(f'{self.marca} {self.modelo} está acelerando com seu motor {self.motor.nome}...')
    
    
class Motor:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
        
    def ligar_motor(self):
        print(f'Motor {self.nome} ligado...')
        
honda = Fabricante('Honda')
mitsubishi = Fabricante('Mitsubishi')

v8 = Motor('V8')
v6 = Motor('V6')

civic = honda.montar_carro('Civic', v8)
lancer = mitsubishi.montar_carro('Lancer', v6)
eclipse = mitsubishi.montar_carro('Eclipse', v8)

honda.listar_carros()
mitsubishi.listar_carros()

civic.acelerar()
        