"""json.dump e json.load utilizando pathlib"""

import json
# import os
from pathlib import Path

NOME_ARQUIVO = 'dump_load_2.json'
# CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(
#     os.path.join(
#         os.path.dirname(__file__),
#         NOME_ARQUIVO
#     )
# )
CAMINHO_ABSOLUTO_ARQUIVO = Path(__file__).absolute().parent / NOME_ARQUIVO

livro = {
    'title': 'A Song of Ice and Fire: A Game of Thrones',
    'title_pt_br': 'As Crônicas de Gelo e Fogo: A Guerra dos Tronos',
    'author': 'George R. R. Martin',
    'pages': 694,
    'main_characters': ['Jon Snow', 'Daenerys Targaryen', 'Ned Stark', 'Cersei Lannister', 'Robert Baratheon'],
    'dragons': ['Drogon', 'Rhaegal', 'Viserion'],
    'is_read': True
}

# with open(CAMINHO_ABSOLUTO_ARQUIVO, 'w') as arquivo:
#     json.dump(livro, arquivo, indent=2)
with CAMINHO_ABSOLUTO_ARQUIVO.open('w') as arquivo:
    json.dump(livro, arquivo, indent=2)

# with open(CAMINHO_ABSOLUTO_ARQUIVO, 'r') as arquivo:
#     livro_json = json.load(arquivo)
#     print(livro_json)
with CAMINHO_ABSOLUTO_ARQUIVO.open('r') as arquivo:
    livro_json = json.load(arquivo)
    print(livro_json)
