"""
Abstração e Mixins
"""

from eletronico import Smartphone

galaxy_s = Smartphone('Samsung', 'Galaxy S')
iphone = Smartphone('Apple', 'iPhone')

galaxy_s.ligar()
galaxy_s.desligar()

iphone.desligar()
iphone.ligar()
iphone.ligar()
iphone.desligar()
