"""os.walk para navegar de caminhos de forma recursiva"""
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).

import os
from itertools import count

caminho = os.path.join('D:/', 'Programacao')
# print(f'{caminho=}')
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(f'{the_counter} | Pasta atual: {root}')
    
    for dir_ in dirs:
        print(f'\t{the_counter} | Subpasta: {dir_}')
        
    for file_ in files:
        print(f'\t{the_counter} | Arquivo: {file_}')
