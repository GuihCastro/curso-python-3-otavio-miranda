"""
Continuação da manipulação de arquivos
    -> Modos de abertura e encoding com `with open`
"""

path = 'aulas\\arquivos\\'
path += 'aula90.txt'

with open(path, 'w', encoding='utf-8') as file: # o windows precisa do parâmetro `encoding` como 'utf-8'
    file.write('Olá, Mundão!')
