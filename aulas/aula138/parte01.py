"""sys.argv - Executando arquivos com argumentos no sistema"""

import sys

argumentos = sys.argv
qtd_argumentos = len(argumentos)

if qtd_argumentos <= 1:
    print('Você não passou argumentos')
else:
    print(f'Você passou o(s) argumento(s) {argumentos[1:]}')
