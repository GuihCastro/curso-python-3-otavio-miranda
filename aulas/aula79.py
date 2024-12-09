"""
Introdução aos pacotes (packages) em Python
    -> As importações SEMPRE devem ser vistas considerando o "ponto de vista" do arquivo `__main__`
"""

import aula79_package.modulo
from aula79_package.modulo import soma
from aula79_package import modulo

print(modulo.soma(6, 6, 6))
modulo.falar_oi()
