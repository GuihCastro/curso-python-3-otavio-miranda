"""
`os.remove()` | `os.unlink()` -> apagar arquivo
`os.rename()` -> renomear / mover arquivo
"""

import os

directory = 'aulas\\arquivos\\'
path = directory + 'aula91.txt'

# with open(path, 'w') as file:
#     file.write('Hello, World!')

new_path = directory+'aula91-02.txt'
# os.rename(path, new_path)

os.remove(new_path)
