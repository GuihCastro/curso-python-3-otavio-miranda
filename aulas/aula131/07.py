"""os + shutil - Apagando, copiando, movendo e renomeando pastas com Python"""
# Copiar -> shutil.copy
# Copiar Árvore recursivamente -> shutil.copytree
# Apagar Árvore recursivamente -> shutil.rmtree
# Apagar arquivos -> os.unlink
# Renomear/Mover -> shutil.move ou os.rename

import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'pasta_original')
NOVA_PASTA = os.path.join(DESKTOP, 'nova_pasta')

shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)
shutil.rmtree(PASTA_ORIGINAL, ignore_errors=True)
shutil.move(NOVA_PASTA, NOVA_PASTA + '_final')

# for root, dirs, files in os.walk(NOVA_PASTA):
#     for dir_ in dirs:
#         os.rmdir(os.path.join(root, dir_))
        
# os.rmdir(PASTA_ORIGINAL)
