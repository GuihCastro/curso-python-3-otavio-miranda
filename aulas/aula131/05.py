"""os.path.getsize e os.stat para dados dos arquivos (tamanho em bytes)"""

import math
import os
from itertools import count


def formata_tamanho(tamanho_em_bytes: int, base: int = 1024) -> str:
    """Formata um tamanho, de bytes, retornando uma string no padrão (1023 -> '1023B', 1024 -> 1KB)"""
    # Original: https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python
    
    if tamanho_em_bytes <= 0:
        # Se o tamanho for menor ou igual a 0, retorna 0B
        return "0B"
    
    # Cria uma lista de tuplas com os prefixos binários e seus expoentes
    prefixos = ('B', 'KB', 'MB', 'GB', 'TB', 'PB')
    
    # math.log vai retornar o logaritmo do tamanho_em_bytes com a base (1024 por padrão), isso deve bater com o índice na abreviação dos tamanhos
    indice_prefixo = int(math.log(tamanho_em_bytes, base))
    # Por quanto o tamanho deve ser dividido para gerar o tamanho correto.
    potencia = base ** indice_prefixo
    # Obtendo o tamanho final, dividindo o tamanho original pela potência
    tamanho_final = tamanho_em_bytes / potencia
    # O prefixo desejado, baseado no índice
    prefixo = prefixos[indice_prefixo]
    return f'{tamanho_final:.2f} {prefixo}'


caminho = os.path.join('D:/', 'Videos')
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(f'{the_counter} | Pasta atual: {root}')

    for dir_ in dirs:
        print(f'\t{the_counter} | Subpasta: {dir_}')

    for file_ in files:
        caminho_completo_arquivo = os.path.join(root, file_)
        tamanho = os.path.getsize(caminho_completo_arquivo)
        print(f'\t{the_counter} | Arquivo: {file_} | Tamanho: {formata_tamanho(tamanho)}')
