"""
hasattr e getattr
"""

string = 'Guilherme'
metodo = 'upper'

if hasattr(string, metodo):
    print(f'Existe o método {metodo}')
    print(getattr(string, metodo)())
else:
    print(f'Não existe o método {metodo}')
