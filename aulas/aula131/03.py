# """os.listdir - para navegar em caminhos

# /Users/luizotavio/Desktop/EXEMPLO
# C:\Users\luizotavio\Desktop\EXEMPLO
# caminho = r'"D:\\Imagens"'
# """

import os

caminho = r'D:/Programacao'

for diretorio in os.listdir(caminho):
    caminho_completo = os.path.join(caminho, diretorio)
    
    if not os.path.isdir(caminho_completo):
        continue
    
    print(f'{diretorio=}')
    for item in os.listdir(caminho_completo):
        print(f'\t{item=}')
