"""string.Template para substituir variáveis em textos"""
#   doc: https://docs.python.org/3/library/string.html#template-strings
#
# Métodos:
#   substitute: substitui mas gera erros se faltar chaves
#   safe_substitute: substitui sem gerar erros
# Também é possível trocar o delimitador e outras coisas criando uma subclasse de template.

import locale
import string
from datetime import datetime
from pathlib import Path

locale.setlocale(locale.LC_ALL, '')

ARQUIVO = 'modelo.txt'
CAMINHO_ARQUIVO = Path(__file__).parent / ARQUIVO


def converte_para_brl(numero: float) -> str:
    brl = 'R$ ' + locale.currency(numero, symbol=False, grouping=True)
    return brl


data = datetime.now()
dados = dict(
    nome='Mari',
    valor=converte_para_brl(6_666_666),
    data=data.strftime('%d/%m/%Y'),
    empresa='GHC Corp.',
    telefone='+55 (11) 96666-6666'
)

with CAMINHO_ARQUIVO.open('r', encoding='utf8') as arquivo:
    texto = arquivo.read()
    template = string.Template(texto)
    print(template.substitute(dados))
