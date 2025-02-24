"""csv.writer e csv.DictWriter para escrever em CSV"""

import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'exemplo-escrita.csv'

lista_clientes = [
    {'Nome': 'Guilherme Castro', 'Endereço': 'Rua Tal, 666'},
    {'Nome': 'Mariana Livraes', 'Endereço': 'Rua Tal, 666'},
    {'Nome': 'Magg Maggie', 'Endereço': 'Rua Tal, 666'},
    {'Nome': 'Kurt Kurtie', 'Endereço': 'Rua Tal, 666'},
    {'Nome': 'Guts Gutsie', 'Endereço': 'Rua Tal, 666'},
    {'Nome': 'Red Redie', 'Endereço': 'Rua Tal, 666'},
]

with CAMINHO_CSV.open('w', encoding='utf-8', ) as arquivo:
    colunas = lista_clientes[0].keys()
    
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=colunas
    )
    
    escritor.writeheader()
    for cliente in lista_clientes:
        escritor.writerow(cliente)
