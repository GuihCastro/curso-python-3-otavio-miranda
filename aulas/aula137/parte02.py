"""ZIP - Compactando / Descompactando arquivos com zipfile.ZipFile"""
# Compactando e descompactando arquivos

import os
import parte01 as src
from zipfile import ZipFile

# Populando o pacote
src.popular_pacote(10, src.CAMINHO_PACOTE)

# Compactando o pacote
with ZipFile(src.CAMINHO_ZIP, 'w') as zip:
    for root, dirs, files in os.walk(src.CAMINHO_PACOTE):
        for file in files:
            zip.write(os.path.join(root, file), file)

# Lendo arquivos do zip
with ZipFile(src.CAMINHO_ZIP, 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)
        
# Descompactando arquivos do pacote
with ZipFile(src.CAMINHO_ZIP, 'r') as zip:
    zip.extractall(src.CAMINHO_PACOTE)
