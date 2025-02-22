"""json.dump e json.load com arquivos"""

import json
import os

NOME_ARQUIVO = 'dump_load.json'
CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        NOME_ARQUIVO
    )
)

livro = {
    'title': 'A Song of Ice and Fire: A Game of Thrones',
    'title_pt_br': 'As Crônicas de Gelo e Fogo: A Guerra dos Tronos',
    'author': 'George R. R. Martin',
    'pages': 694,
    'main_characters': ['Jon Snow', 'Daenerys Targaryen', 'Ned Stark', 'Cersei Lannister', 'Robert Baratheon'],
    'dragons': ['Drogon', 'Rhaegal', 'Viserion'],
    'is_read': True
}

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'w') as arquivo:
    json.dump(livro, arquivo, indent=2)

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'r') as arquivo:
    livro_json = json.load(arquivo)
    print(livro_json)
    