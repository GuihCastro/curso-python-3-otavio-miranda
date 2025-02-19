"""Módulos para interação com o sistema operacional - os
Doc: https://docs.python.org/3/library/os.html

O módulo `os` fornece funções para interagir com o sistema operacional.
Por exemplo, o módulo os.path contém funções para trabalhar com caminhos de arquivos e a função os.listdir() pode ser usada para listar os arquivos em um diretório. 
O método os.system() permite executar comandos do sistema operacional a partir do código Python.

Windows 11 (PowerShell), Linux, Mac = clear
Windows (antigo, cmd) = cls
"""

import os
from time import sleep

os.system('echo Hello, World!')

sleep(5)

os.system('clear')

print('a' * 80)
print('a' * 80)
print('a' * 80)
print('a' * 80)
print('a' * 80)
print('a' * 80)
